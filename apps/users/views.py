from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, logout, authenticate

from .models import UserProfile
from .forms import LoginForm
# Create your views here.


class LoginView(View):
    """
    用户登陆
    """
    def get(self, request):
        register_form = LoginForm()
        return render(request, "login.html", {"login_form": register_form})

    def post(self, request):
        login_from = LoginForm(request.POST)
        if login_from.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(
                    request,
                    "login.html",
                    {"msg": "用户名或密码错误", "login_form": login_from}
                )
        else:
            return render(
                request,
                "login.html",
                {"login_form": login_from}
            )

class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


