import markdown

from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, Count

from .models import Post, Categort, Tag
from .forms import CommentFrom
# Create your views here.


# 首页视图
class IndexView(View):

    def get(self, request):
        all_post = Post.objects.all()

        categroty = request.GET.get('categroty', '')
        if categroty:
            all_post = all_post.filter(category__text=categroty)

        year = request.GET.get('year', '')
        month = request.GET.get('month', '')
        if year and month:
            all_post = Post.objects.filter(created_time__year=year,
                                            created_time__month=month
                                            ).order_by('-created_time')

        all_post = all_post.order_by("-created_time")
        page = Paginator(all_post,3)
        page_num = request.GET.get('page', 1)
        try:
            page = page.page(page_num)
        except PageNotAnInteger:
            # 如果页面不是整数，则传递第一页。
            page = page.page(1)
        except EmptyPage:
            # 如果页面超出范围，则返回最后一页的结果。
            page = page.page(page.num_pages)


        return render(request, 'sub-index.html', {
            'all_post': page,
        })


# 文章视图
class ArticleView(View):

    def get(self, request, id):
        try:
            article = Post.objects.get(id=id)
        except:
            return HttpResponseRedirect(reverse('index'))
        article.body = markdown.markdown(article.body)

        comment_list = article.comments_set.all()
        article.increase_views()
        return render(request, 'sub-single.html', {
            'article': article,
            'comment_list': comment_list,
        })

    def post(self, request, id):
        article = Post.objects.get(id=id)
        article.body = markdown.markdown(article.body)
        form = CommentFrom(request.POST)
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.post = article
            # 最终保存到数据库
            comment.save()
            return HttpResponseRedirect(reverse('article', args=[id]))
        else:
            comment_list = article.comments_set.all()
            return render(request, 'sub-single.html', {
                'article': article,
                'comment_list': comment_list,
                'form':form,
            })


# 文章列表视图
class BlogListView(View):

    def get(self, request):
        all_post = Post.objects.all()
        return render(request, 'sub-full-width.html', {
            'all_post': all_post
        })