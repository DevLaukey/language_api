from django.db import models

# Model for storing English phrases and auxiliary verbs
class EnglishPhrase(models.Model):
    phrase = models.CharField(max_length=255)
    
    def __str__(self):
        return self.phrase

# Model for storing example sentences related to each English phrase
class ExampleSentence(models.Model):
    phrase = models.ForeignKey(EnglishPhrase, on_delete=models.CASCADE, related_name='example_sentences')
    sentence = models.TextField()
    
    def __str__(self):
        return self.sentence

# Model for storing exercise questions
class Exercise(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Model for storing exercise questions
class ExerciseQuestion(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return self.text

# Model for storing choices related to each exercise question
class QuestionChoice(models.Model):
    question = models.ForeignKey(ExerciseQuestion, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct_choice = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text

