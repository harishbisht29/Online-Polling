from django.contrib import admin

# Register your models here.
from .models import Survey_Templates
from .models import Question_Survey

admin.site.register(Survey_Templates)
admin.site.register(Question_Survey)