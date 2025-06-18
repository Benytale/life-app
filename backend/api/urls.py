from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet, UserViewSet, EarningViewSet

router = DefaultRouter()
router.register('videos', VideoViewSet)
router.register('users', UserViewSet)
router.register('earnings', EarningViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
