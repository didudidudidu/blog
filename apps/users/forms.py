#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错        误"})