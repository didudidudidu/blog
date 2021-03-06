from django.contrib import admin

from .models import Post, Categort, Tag, Comments, Reply
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titel', 'excerpt', 'category', 'created_time', 'modified_time', 'user']
    filter_vertical = ('tag',)


@admin.register(Categort)
class CategortAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['text']


admin.site.site_title = '博客管理系统'
admin.site.site_header = '个人博客博客'
