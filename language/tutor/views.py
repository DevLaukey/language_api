from rest_framework import viewsets
from .models import EnglishPhrase, ExampleSentence, Exercise, ExerciseQuestion, QuestionChoice
from .serializers import EnglishPhraseSerializer, ExampleSentenceSerializer, ExerciseSerializer, ExerciseQuestionSerializer, QuestionChoiceSerializer

# Viewset for EnglishPhrase model
class EnglishPhraseViewSet(viewsets.ModelViewSet):
    queryset = EnglishPhrase.objects.all()
    serializer_class = EnglishPhraseSerializer

# Viewset for ExampleSentence model
class ExampleSentenceViewSet(viewsets.ModelViewSet):
    queryset = ExampleSentence.objects.all()
    serializer_class = ExampleSentenceSerializer

# Viewset for Exercise model
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

# Viewset for ExerciseQuestion model
class ExerciseQuestionViewSet(viewsets.ModelViewSet):
    queryset = ExerciseQuestion.objects.all()
    serializer_class = ExerciseQuestionSerializer

# Viewset for QuestionChoice model
class QuestionChoiceViewSet(viewsets.ModelViewSet):
    queryset = QuestionChoice.objects.all()
    serializer_class = QuestionChoiceSerializer
