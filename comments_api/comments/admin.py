from django.contrib import admin
from .models import Article, Comment, CommentAnswer


@admin.register(Article, Comment, CommentAnswer)
class ArticleAdmin(admin.ModelAdmin):
    pass
