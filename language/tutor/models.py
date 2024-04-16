from django.db import models

# Create your models here.
from django.db import models

# Model for storing English phrases and auxiliary verbs
class EnglishPhrase(models.Model):
    phrase = models.CharField(max_length=255, unique=True, help_text='English phrase or auxiliary verb')
    
    def __str__(self):
        return self.phrase

# Model for storing example sentences related to each English phrase
class ExampleSentence(models.Model):
    phrase = models.ForeignKey(EnglishPhrase, on_delete=models.CASCADE, related_name='example_sentences')
    sentence = models.TextField(help_text='Example sentence using the English phrase')
    
    def __str__(self):
        return self.sentence

# Model for storing user profiles (if you plan to implement user-specific features)
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    # Add fields for additional user-related data if needed
    
    def __str__(self):
        return self.user.username
