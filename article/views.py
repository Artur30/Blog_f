from django.shortcuts import render, render_to_response, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404
from article.models import Article, Comments
from article.forms import CommentForm, NewState
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.utils import timezone
from blog import settings


def articles(request, page_number=1):
    """
    The function calculates all published articles, sorts them in descending
    order of time, there is a paginator, passesit to the template.
    :param request:
    :param page_number:
    :return:
    """
    all_articles_published = Article.objects.filter(article_published=1).order_by('-article_date')
    current_page = Paginator(all_articles_published, per_page=settings.Number_Articles_On_Page)
    articles_page = current_page.page(page_number)
    user = auth.get_user(request)

    tags = []
    for obj in all_articles_published:
        tags += obj.article_tags.names()

    context = {'articles': articles_page, 'user': user, 'tags': tags}
    return render(request, 'article/articles.html', context)


def article(request, article_id=1, comments_page_number=1):
    """
    The function calculates the elements of a single article
    :param request:
    :param article_id:
    :param comments_page_number:
    :return:
    """
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['user'] = auth.get_user(request)
    # Пагинация комментариев
    current_comments_page = Paginator(args['comments'], per_page=settings.Number_Comments_On_Page)
    args['comments'] = current_comments_page.page(comments_page_number)

    return render(request, 'article/article.html', args)


def add_like(request, page_number, article_id):
    """
    The function adds like of the article
    :param request:
    :param page_number:
    :param article_id:
    :return:
    """
    all_articles = Article.objects.filter(article_published=1).order_by('-article_date')
    current_page = Paginator(all_articles, per_page=settings.Number_Articles_On_Page)
    articles_page = current_page.page(page_number)
    user = auth.get_user(request)

    if request.user.is_authenticated:
        users = User.objects.filter(users_article_main=article_id)
        current_user = request.user

        if current_user not in users:
            article = get_object_or_404(Article, pk=article_id)
            article.article_likes += 1
            article.users_likes.add(current_user)
            article.save()

    context = {'articles': articles_page, 'user': user}
    return render(request, 'article/articles.html', context)


def add_comment(request, article_id):
    """
    The function adds comment of the article
    :param request:
    :param article_id:
    :return:
    """
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_date = timezone.now()

            if request.user.id:
                comment.comments_from_id = request.user.id
            else:
                return HttpResponse('Не авторизован')

            form.save()
            # Создаем объект сессии в течении 60 секунд
            # request.session.set_expiry(60)
            # request.session['pause'] = True
    return redirect(reverse('article:article', args=(article_id, 1)))


def suggest_article(request):
    """
    The function preposes new article
    :param request:
    :return:
    """
    args = {}
    args.update(csrf(request))
    args['form'] = NewState

    if request.POST:
        form = NewState(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.article_date = timezone.now()
            article.article_published = False

            article.article_author += auth.get_user(request).last_name + ' '
            article.article_author += auth.get_user(request).first_name + ' '
            article.article_author += '(' + auth.get_user(request).username + ')'
            article.save()
            return redirect(reverse('article:articles'))
    else:
        return render(request, 'suggest_article/index.html', args)
    return render(request, 'suggest_article/index.html', args)


def articles_tag(request, tag, page_number=1):
    """
    Function for working with tags.
    :param request:
    :param tag:
    :param page_number:
    :return:
    """
    all_articles_published = Article.objects.filter(
        article_published=1
    ).filter(
        article_tags__name=tag
    ).order_by('-article_date')

    current_page = Paginator(all_articles_published, per_page=settings.Number_Articles_On_Page)
    articles_page = current_page.page(page_number)

    tags = []
    for obj in Article.objects.filter(article_published=1):
        tags += obj.article_tags.names()

    context = {'articles': articles_page, 'tags': tags}
    return render(request, 'article/articles_tag.html', context)
















