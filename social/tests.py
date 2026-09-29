from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from tempfile import TemporaryDirectory
from io import BytesIO
from PIL import Image

from .models import Post, Like, Comment, Follow, Profile, Bookmark


class SocialPlatformFlowTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username='alice', email='alice@example.com', password='StrongPass123')
        self.bob = User.objects.create_user(username='bob', email='bob@example.com', password='StrongPass123')

    def test_profiles_created_for_users(self):
        self.assertTrue(Profile.objects.filter(user=self.alice).exists())
        self.assertTrue(Profile.objects.filter(user=self.bob).exists())

    def test_registration_creates_and_logs_in_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'charlie',
            'email': 'charlie@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='charlie').exists())
        self.assertTrue(Profile.objects.filter(user__username='charlie').exists())
        self.assertTrue(response.context['user'].is_authenticated)

    def test_post_like_comment_follow_and_search_flow(self):
        self.client.login(username='alice', password='StrongPass123')

        create = self.client.post(reverse('create_post'), {
            'content': 'My first CampusCircle post',
            'image_url': '',
        }, follow=True)
        self.assertEqual(create.status_code, 200)
        post = Post.objects.get(author=self.alice)
        self.assertEqual(post.content, 'My first CampusCircle post')

        self.client.post(reverse('logout'))
        self.client.login(username='bob', password='StrongPass123')

        like = self.client.post(reverse('toggle_like', args=[post.pk]), {'next': reverse('feed')}, follow=True)
        self.assertEqual(like.status_code, 200)
        self.assertTrue(Like.objects.filter(user=self.bob, post=post).exists())

        comment = self.client.post(reverse('add_comment', args=[post.pk]), {
            'content': 'Nice post!', 'next': reverse('feed')
        }, follow=True)
        self.assertEqual(comment.status_code, 200)
        self.assertTrue(Comment.objects.filter(author=self.bob, post=post, content='Nice post!').exists())

        follow = self.client.post(reverse('toggle_follow', args=['alice']), follow=True)
        self.assertEqual(follow.status_code, 200)
        self.assertTrue(Follow.objects.filter(follower=self.bob, following=self.alice).exists())

        search = self.client.get(reverse('search_users'), {'q': 'bob'})
        self.assertContains(search, 'bob')  # current user is searchable too

    def test_follow_toggle_unfollows(self):
        self.client.login(username='alice', password='StrongPass123')
        self.client.post(reverse('toggle_follow', args=['bob']))
        self.assertTrue(Follow.objects.filter(follower=self.alice, following=self.bob).exists())
        self.client.post(reverse('toggle_follow', args=['bob']))
        self.assertFalse(Follow.objects.filter(follower=self.alice, following=self.bob).exists())

    def test_like_toggle_unlikes(self):
        post = Post.objects.create(author=self.alice, content='Toggle like test')
        self.client.login(username='bob', password='StrongPass123')
        self.client.post(reverse('toggle_like', args=[post.pk]))
        self.client.post(reverse('toggle_like', args=[post.pk]))
        self.assertFalse(Like.objects.filter(user=self.bob, post=post).exists())

    def test_explore_page_loads_posts(self):
        Post.objects.create(author=self.alice, content='Explore me')
        self.client.login(username='bob', password='StrongPass123')
        response = self.client.get(reverse('explore'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Explore me')

    def test_image_upload_is_saved(self):
        with TemporaryDirectory() as tmp:
            with override_settings(MEDIA_ROOT=tmp):
                self.client.login(username='alice', password='StrongPass123')
                bytes_out = BytesIO()
                Image.new('RGB', (4, 4), '#fbd178').save(bytes_out, 'PNG')
                upload = SimpleUploadedFile('photo.png', bytes_out.getvalue(), content_type='image/png')
                response = self.client.post(reverse('create_post'), {
                    'content': 'Photo post',
                    'image': upload,
                    'image_url': '',
                }, follow=True)
                self.assertEqual(response.status_code, 200)
                post = Post.objects.get(content='Photo post')
                self.assertTrue(post.image.name.endswith('.png'))

    def test_topic_filter_and_saved_posts_flow(self):
        build = Post.objects.create(author=self.alice, content='Shipping our prototype', topic='BUILD')
        Post.objects.create(author=self.alice, content='Upcoming design meetup', topic='EVENTS')
        self.client.login(username='bob', password='StrongPass123')
        filtered = self.client.get(reverse('feed'), {'topic': 'BUILD'})
        self.assertContains(filtered, 'Shipping our prototype')
        self.assertNotContains(filtered, 'Upcoming design meetup')
        self.client.post(reverse('toggle_bookmark', args=[build.id]))
        self.assertTrue(Bookmark.objects.filter(user=self.bob, post=build).exists())
        self.assertContains(self.client.get(reverse('saved_posts')), 'Shipping our prototype')
