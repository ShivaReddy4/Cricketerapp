from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CricketerViewSet

from .views import CricketerListCreateView

router = DefaultRouter()
router.register(r'cricketers', CricketerViewSet)

urlpatterns = [
    path('cricketers/', CricketerListCreateView.as_view(), name='cricketer-list'),
]
urlpatterns = router.urls
