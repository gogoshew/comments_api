from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = '__all__'
        depth = 3


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
