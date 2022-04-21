from rest_framework import viewsets

from comments.models import Comment, CommentAnswer
from comments.serializers import CommentSerializer, CommentAnswerSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AnswersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CommentAnswer.objects.all()
    serializer_class = CommentAnswerSerializer
