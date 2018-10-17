#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.db.models import Sum, Count

from blog_app.models import Post, Tag


def context(request):
    all_post = Post.objects.all()
    # 分类
    categroty_sum = all_post.annotate(count=Count('category')).values('category__text', 'count')
    # 归档
    # dates():返回不同月份的值的列表
    archiving = all_post.dates('created_time', 'month', order='DESC')
    # 最热文章
    hot_post = all_post.order_by("-created_time")[:3]
    all_tag = Tag.objects.all()
    return {
        'categroty_sum': categroty_sum,
        'all_tag': all_tag,
        'hot_post': hot_post,
        'archiving': archiving,
    }
