from rest_framework import viewsets
from rest_framework.response import Response
from .models import EnglishPhrase, ExampleSentence
from rest_framework import serializers
from .serializers import EnglishPhraseSerializer, ExampleSentenceSerializer

# Serializer classes
class EnglishPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishPhrase
        fields = '__all__'

class ExampleSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleSentence
        fields = '__all__'

# Viewsets
class EnglishPhraseViewSet(viewsets.ModelViewSet):
    queryset = EnglishPhrase.objects.all()
    serializer_class = EnglishPhraseSerializer

class ExampleSentenceViewSet(viewsets.ModelViewSet):
    queryset = ExampleSentence.objects.all()
    serializer_class = ExampleSentenceSerializer
