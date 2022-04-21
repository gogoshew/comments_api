from rest_framework import serializers
from .models import Article, Comment, CommentAnswer


class CommentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentAnswer
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    # Включаем все ответы на комментарий
    answers = CommentAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
