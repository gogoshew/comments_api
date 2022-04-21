from django.db import models


class Article(models.Model):
    article_name = models.CharField(max_length=200, verbose_name='Статья')
    pub_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    article_description = models.CharField(max_length=200, verbose_name='Содержание статьи')

    def __str__(self):
        return self.article_name


class Comment(models.Model):
    comment_text = models.CharField(max_length=200, verbose_name='Текст комментария')
    pub_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, related_name='comment', verbose_name='Комментарий', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text


class CommentAnswer(models.Model):
    answer_text = models.CharField(max_length=200, verbose_name='Ответ', null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, related_name='comment', verbose_name='Ответ', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text
