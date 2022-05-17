from django.urls import path, include
from .views import UserMessageViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('messages', UserMessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]
