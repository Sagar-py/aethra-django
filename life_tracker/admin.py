from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import System, Question, Review, Answer

admin.site.register(System)
admin.site.register(Question)
admin.site.register(Review)
admin.site.register(Answer)