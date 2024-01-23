from django.contrib import admin
from .models import Sentences
from .models import Document
from .models import POS

# Register your models here.

admin.site.register(Sentences)
admin.site.register(Document)
admin.site.register(POS)
