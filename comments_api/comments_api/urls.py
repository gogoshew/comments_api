from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from comments.views import ArticleViewSet, AnswersViewSet

router = routers.SimpleRouter()
router.register(r'comments', ArticleViewSet)
router.register(r'answers', AnswersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
