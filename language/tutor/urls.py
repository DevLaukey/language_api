from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnglishPhraseViewSet, ExampleSentenceViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'english-phrases', EnglishPhraseViewSet)
router.register(r'example-sentences', ExampleSentenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]