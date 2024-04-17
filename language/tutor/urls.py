from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnglishPhraseViewSet, ExampleSentenceViewSet, ExerciseViewSet, ExerciseQuestionViewSet, QuestionChoiceViewSet

# Create a router and register viewsets
router = DefaultRouter()

router.register(r'english-phrases', EnglishPhraseViewSet, basename='englishphrase')
router.register(r'example-sentences', ExampleSentenceViewSet, basename='examplesentence')
router.register(r'exercises', ExerciseViewSet, basename='exercise')
router.register(r'exercise-questions', ExerciseQuestionViewSet, basename='exercisequestion')
router.register(r'question-choices', QuestionChoiceViewSet, basename='questionchoice')

urlpatterns = [
    path('', include(router.urls)),
]
