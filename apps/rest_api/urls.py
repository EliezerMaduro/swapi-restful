from rest_framework.routers import DefaultRouter
from django.urls import path, include
#from .views import MiModeloViewSet

router = DefaultRouter()
#router.register(r'mimodelo', MiModeloViewSet, basename='mimodelo')

urlpatterns = [
    path('', include(router.urls)),
]