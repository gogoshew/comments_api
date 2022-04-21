from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .yasg import urlpatterns as doc_urls

from comments.views import ArticleViewSet, AnswersViewSet

router = routers.SimpleRouter()
router.register(r'comments', ArticleViewSet)
router.register(r'answers', AnswersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += doc_urls