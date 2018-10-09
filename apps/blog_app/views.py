import markdown

from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, Count

from .models import Post, Categort, Tag, Comments
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
        article.update_comments_num()
        return render(request, 'sub-single.html', {
            'article': article,
            'comment_list': comment_list,
        })


# 文章列表视图
class BlogListView(View):

    def get(self, request):
        all_post = Post.objects.all()
        return render(request, 'sub-full-width.html', {
            'all_post': all_post
        })


# 评论
class CommentsView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponse(
                '{"status":"fail", "msg":"用户未登录"}',
                content_type='application/json'
            )
        article_id = request.POST.get("article_id", 0)
        comments = request.POST.get("comments", "")

        form = CommentFrom(request.POST)
        if int(article_id) > 0 and comments:
            course_comments = Comments()
            article = Post.objects.get(id=article_id)
            course_comments.user = request.user
            course_comments.post = article
            course_comments.text = comments
            course_comments.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')
