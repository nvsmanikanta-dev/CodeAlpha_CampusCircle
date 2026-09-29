from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import CommentForm, PostForm, ProfileForm, RegisterForm
from .models import Bookmark, Comment, Follow, Like, Post, Profile


def back_to(request, fallback='feed'):
    next_url = request.POST.get('next', '')
    return redirect(next_url if url_has_allowed_host_and_scheme(next_url, {request.get_host()}) else fallback)


def post_list():
    return Post.objects.select_related('author', 'author__profile').prefetch_related('likes', 'comments__author')


def interactions(user, posts):
    ids = list(posts.values_list('id', flat=True))
    return {
        'liked': set(Like.objects.filter(user=user, post_id__in=ids).values_list('post_id', flat=True)),
        'bookmarked': set(Bookmark.objects.filter(user=user, post_id__in=ids).values_list('post_id', flat=True)),
    }


def register(request):
    if request.user.is_authenticated:
        return redirect('feed')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Welcome to CampusCircle!')
        return redirect('feed')
    return render(request, 'registration/register.html', {'form': form})


@login_required
def feed(request):
    posts = post_list()
    topic = request.GET.get('topic', '').upper()
    if topic in dict(Post.TOPICS):
        posts = posts.filter(topic=topic)
    else:
        topic = ''
    following = request.GET.get('view') == 'following'
    if following:
        followed_ids = Follow.objects.filter(follower=request.user).values_list('following_id', flat=True)
        posts = posts.filter(Q(author=request.user) | Q(author_id__in=followed_ids))
    followed_ids = Follow.objects.filter(follower=request.user).values_list('following_id', flat=True)
    suggested = User.objects.exclude(id=request.user.id).exclude(id__in=followed_ids).select_related('profile')[:4]
    context = {
        'posts': posts, 'topics': Post.TOPICS, 'selected_topic': topic,
        'following_view': following, 'post_form': PostForm(), 'suggested': suggested,
    }
    context.update(interactions(request.user, posts))
    return render(request, 'social/feed.html', context)


@login_required
@require_POST
def create_post(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, 'Your post is live.')
    else:
        messages.error(request, 'Post could not be published. Check the text, link and image size.')
    return redirect('feed')


@login_required
@require_POST
def delete_post(request, pk):
    get_object_or_404(Post, pk=pk, author=request.user).delete()
    messages.success(request, 'Post removed.')
    return back_to(request)


@login_required
@require_POST
def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return back_to(request)


@login_required
@require_POST
def toggle_bookmark(request, pk):
    post = get_object_or_404(Post, pk=pk)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, post=post)
    if not created:
        bookmark.delete()
    return back_to(request)


@login_required
@require_POST
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
    else:
        messages.error(request, 'Write a comment before posting.')
    return back_to(request)


@login_required
def profile_view(request, username):
    account = get_object_or_404(User, username=username)
    profile, _ = Profile.objects.get_or_create(user=account)
    posts = post_list().filter(author=account)
    context = {
        'profile_user': account, 'profile': profile, 'posts': posts,
        'is_following': Follow.objects.filter(follower=request.user, following=account).exists() if account != request.user else False,
        'followers_count': account.follower_relations.count(),
        'following_count': account.following_relations.count(),
    }
    context.update(interactions(request.user, posts))
    return render(request, 'social/profile.html', context)


@login_required
@require_POST
def toggle_follow(request, username):
    target = get_object_or_404(User, username=username)
    if target != request.user:
        relation, created = Follow.objects.get_or_create(follower=request.user, following=target)
        if not created:
            relation.delete()
    return redirect('profile', username=username)


@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save(update_fields=['first_name', 'last_name', 'email'])
            messages.success(request, 'Profile saved.')
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile, initial={
            'first_name': request.user.first_name, 'last_name': request.user.last_name,
            'email': request.user.email,
        })
    return render(request, 'social/edit_profile.html', {'form': form})


@login_required
def explore(request):
    posts = post_list()
    topic = request.GET.get('topic', '').upper()
    if topic in dict(Post.TOPICS):
        posts = posts.filter(topic=topic)
    else:
        topic = ''
    return render(request, 'social/explore.html', {
        'posts': posts, 'topics': Post.TOPICS, 'selected_topic': topic,
    })


@login_required
def saved_posts(request):
    posts = post_list().filter(bookmarks__user=request.user)
    context = {'posts': posts}
    context.update(interactions(request.user, posts))
    return render(request, 'social/saved.html', context)


@login_required
def search_users(request):
    q = request.GET.get('q', '').strip()[:80]
    users = User.objects.none()
    if q:
        users = User.objects.filter(
            Q(username__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q)
        ).select_related('profile')[:20]
    return render(request, 'social/search.html', {'q': q, 'users': users})
