from django.db import models
from django.conf import settings

# Create your models here.

class Sentences(models.Model):
	text = models.TextField(blank=True,null=True)

	def __str__(self):
		model_name = self.__class__.__name__
		fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
		return f"{model_name}({fields_str})"




class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
    	model_name = self.__class__.__name__
    	fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
    	return f"{model_name}({fields_str})"

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

	def __str__(self):
		model_name = self.__class__.__name__
		fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
		return f"{model_name}({fields_str})"
