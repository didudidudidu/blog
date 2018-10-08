#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms

from .models import Comments


class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'text', 'url']