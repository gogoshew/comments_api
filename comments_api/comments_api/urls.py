from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .yasg import urlpatterns as doc_urls

from comments.views import ArticleViewSet, AnswersViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'answers', AnswersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += doc_urls
