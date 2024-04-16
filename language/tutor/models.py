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

# Model for storing user profiles (if you plan to implement user-specific features)
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    
    def __str__(self):
        return self.user.username
