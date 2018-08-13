#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.db.models import Sum, Count

from .models import Post, Tag

def context(request):
    all_post = Post.objects.all()
    categroty_sum = all_post.values('category_id').annotate(count=Count('category')).values('category__text', 'count')
    archiving_sum = all_post.dates('created_time','month',order='DESC')
    hot_post = all_post.order_by("-created_time")[:3]
    all_tag = Tag.objects.all()
    return {
        'categroty_sum': categroty_sum,
        'all_tag': all_tag,
        'hot_post': hot_post,
        'archiving_sum': archiving_sum,
    }