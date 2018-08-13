from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Categort(models.Model):
    text = models.CharField(max_length=20, verbose_name='分类名')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '分类表'
        verbose_name_plural = '分类表'


class Tag(models.Model):
    text = models.CharField(max_length=20, null=True, blank=True,verbose_name='标签名')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '标签表'
        verbose_name_plural = '标签表'


class Post(models.Model):
    titel = models.CharField(max_length=100, verbose_name='文章标题')
    body = models.TextField(verbose_name='文章内容')
    excerpt = models.CharField(max_length=200, verbose_name='摘要')
    category = models.ForeignKey(Categort, on_delete=models.CASCADE, verbose_name='分类')
    tag = models.ManyToManyField(Tag)
    created_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    modified_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = '文章表'


class Comments(models.Model):
    name = models.CharField(max_length=10, verbose_name='用户名称')
    email = models.EmailField(verbose_name='邮箱地址')
    text = models.TextField(verbose_name='评论内容')
    url = models.URLField(verbose_name='网址')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='文章')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '评论表'
        verbose_name_plural = '评论表'