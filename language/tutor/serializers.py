from rest_framework import serializers
from django.contrib.auth.models import User

from .models import EnglishPhrase, ExampleSentence, Exercise, ExerciseQuestion, QuestionChoice



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ExampleSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleSentence
        fields = ('id', 'sentence')

class EnglishPhraseSerializer(serializers.ModelSerializer):
    example_sentences = ExampleSentenceSerializer(many=True, read_only=True)
    
    class Meta:
        model = EnglishPhrase
        fields = ('id', 'phrase', 'example_sentences')

class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = ('id', 'text')

class ExerciseQuestionSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = ExerciseQuestion
        fields = ('id', 'text', 'choices', 'correct_choice')

class ExerciseSerializer(serializers.ModelSerializer):
    questions = ExerciseQuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Exercise
        fields = ('id', 'title', 'is_done', 'created_at', 'questions')
