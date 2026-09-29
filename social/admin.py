from django.contrib import admin
from .models import Profile,Follow,Post,Like,Comment,Bookmark
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): list_display=('user','location','created_at'); search_fields=('user__username','bio')
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin): list_display=('follower','following','created_at')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('author','topic','short_content','created_at')
    list_filter=('topic','created_at')
    search_fields=('author__username','content')
    def short_content(self,obj): return obj.content[:50]
class LikeAdmin(admin.ModelAdmin): list_display=('user','post','created_at')
admin.site.register(Like,LikeAdmin)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): list_display=('author','post','created_at')
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin): list_display=('user','post','created_at')
