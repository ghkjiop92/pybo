from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question)

# Register your models here.
