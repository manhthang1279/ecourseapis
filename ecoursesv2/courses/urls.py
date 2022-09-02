from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, 'category')
router.register('courses', views.CourseViewSet, 'course')
router.register('lessons', views.LessonViewSet, 'lesson')
router.register('users', views.UserViewSet, 'user')
router.register('comments', views.CommentViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view())
]