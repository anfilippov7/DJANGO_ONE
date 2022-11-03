from django.contrib import admin

from .models import Article, TopicsArticle

class ArticleTopicsInline(admin.TabularInline):
    model = TopicsArticle
    extra = 2



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['title']
    # prepopulated_fields = {'title': ('id',),}
    inlines = [ArticleTopicsInline]
    pass



# @admin.register(TopicsArticle)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['topics', 'tags', 'main', 'delete']
#     list_display_links = ['tags']
#     list_editable = ['delete']
#     # prepopulated_fields = {'title': ('id',),}
#     inlines = [ArticleTopicsInline]
#     pass