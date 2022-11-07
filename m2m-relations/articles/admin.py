from django.contrib import admin

from .models import Article, ArticleScope, Tag

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['title']
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']



