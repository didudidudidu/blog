from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect
from django.views.generic.base import View

from .models import Post, Categort, Tag
# Create your views here.


class IndexView(View):

    def get(self, request):
        all_post = Post.objects.all()
        all_categrot = Categort.objects.all()
        all_tag = Tag.objects.all()
        return render(request, 'sub-index.html', {'all_post': all_post, 'all_categrot': all_categrot, 'all_tag': all_tag})


class ArticleView(View):

    def get(self, request, id):
        article = Post.objects.get(id=id)
        all_categrot = Categort.objects.all()
        all_tag = Tag.objects.all()
        if article:
            return render(request, 'sub-single.html', {'article': article, 'all_categrot': all_categrot, 'all_tag': all_tag})
        else:
            return HttpResponseRedirect(reverse('index'))