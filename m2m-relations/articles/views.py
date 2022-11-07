from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles_object = Article.objects.order_by(ordering)
    context = {
        'object_list': articles_object
    }
    return render(request, template, context)
