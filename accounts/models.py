from django.db import models
from django.conf import settings

# Create your models here.

class Sentences(models.Model):
	text = models.TextField(blank=True,null=True)




class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Document(models.Model):
	description = models.CharField(max_length=255, blank=True)
	document= models.FileField(upload_to='document/')
	upload_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.document


class POS(models.Model):
	sentence = models.DecimalField(decimal_places=2,max_digits=1000)
	noun = models.DecimalField(decimal_places=2,max_digits=1000)
	verb = models.DecimalField(decimal_places=2,max_digits=1000)
	adjective = models.DecimalField(decimal_places=2,max_digits=1000)
	adverb = models.DecimalField(decimal_places=2,max_digits=1000)
	article= models.DecimalField(decimal_places=2,max_digits=1000)
	proposition = models.DecimalField(decimal_places=2,max_digits=1000)
	space= models.DecimalField(decimal_places=2,max_digits=1000)
	pronoun = models.DecimalField(decimal_places=2,max_digits=1000)
	Question_word = models.DecimalField(decimal_places=2,max_digits=1000)
	punctation = models.DecimalField(decimal_places=2,max_digits=1000)