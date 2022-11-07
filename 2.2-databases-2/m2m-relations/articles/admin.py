from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleScope, Tag


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                count += 1
            if count > 1:
                raise ValidationError('Основным может быть только один раздел!')
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['title']
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']












# class ArticleScopeInline(admin.TabularInline):
#     model = ArticleScope
#     formset = ArticleScopeInlineFormset


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [ArticleScopeInline]




# class RelationshipInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             # В form.cleaned_data будет словарь с данными
#             # каждой отдельной формы, которые вы можете проверить
#             form.cleaned_data
#             # вызовом исключения ValidationError можно указать админке о наличие ошибки
#             # таким образом объект не будет сохранен,
#             # а пользователю выведется соответствующее сообщение об ошибке
#             raise ValidationError('Тут всегда ошибка')
#         return super().clean()  # вызываем базовый код переопределяемого метода
#
#
# class RelationshipInline(admin.TabularInline):
#     model = Relationship
#     formset = RelationshipInlineFormset
#
#
# @admin.register(Object)
# class ObjectAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]
