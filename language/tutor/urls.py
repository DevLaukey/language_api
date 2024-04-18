from django.urls import path, include
from django.contrib.auth.models import User


from rest_framework.routers import DefaultRouter
from .views import EnglishPhraseViewSet, ExampleSentenceViewSet, ExerciseViewSet, ExerciseQuestionViewSet, QuestionChoiceViewSet, UserRegistrationView

# Create a router and register viewsets
router = DefaultRouter()

router.register(r'english-phrases', EnglishPhraseViewSet, basename='englishphrase')
router.register(r'example-sentences', ExampleSentenceViewSet, basename='examplesentence')
router.register(r'exercises', ExerciseViewSet, basename='exercise')
router.register(r'exercise-questions', ExerciseQuestionViewSet, basename='exercisequestion')
router.register(r'question-choices', QuestionChoiceViewSet, basename='questionchoice')
router.register(r'register', UserRegistrationView, basename='register')
urlpatterns = [
    path('auth/', include('rest_auth.urls'), name='auth'),
    path('', include(router.urls)),

]
