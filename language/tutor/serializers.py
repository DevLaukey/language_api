from rest_framework import serializers
from .models import EnglishPhrase, ExampleSentence

class EnglishPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishPhrase
        fields = '__all__'

class ExampleSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleSentence
        fields = '__all__'
