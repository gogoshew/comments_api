from rest_framework import viewsets

from comments.models import Comment, CommentAnswer, Article
from comments.serializers import ArticleSerializer, CommentSerializer, CommentAnswerSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AnswersViewSet(viewsets.ModelViewSet):
    queryset = CommentAnswer.objects.all()
    serializer_class = CommentAnswerSerializer
