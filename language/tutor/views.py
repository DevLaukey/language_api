from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from .models import EnglishPhrase, ExampleSentence, Exercise, ExerciseQuestion, QuestionChoice
from .serializers import EnglishPhraseSerializer, ExampleSentenceSerializer, ExerciseSerializer, ExerciseQuestionSerializer, QuestionChoiceSerializer, UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (BasicAuthentication, TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        # Override the create method to hash the password before saving the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Manually set the password, as the serializer only returns hashed passwords
        user.set_password(request.data['password'])
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
