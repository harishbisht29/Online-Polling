from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

class Survey_Templates(models.Model):
    NAME_CHOICES = [
       ("Question_Survey","Question_Survey") 
    ]
    name = models.CharField(max_length=20,
    choices = NAME_CHOICES,
    default="Question_Survey",
    unique=True)
    desc = models.CharField(max_length=1000)
    thumbnail = models.ImageField(upload_to='images/')
    date_created = models.DateTimeField()
    input_template = models.CharField(max_length=50, default="survey_template")
    output_template = models.CharField(max_length=50, default="survey_template")

    def __str__(self):
        return self.name
    
    def summary(self):
        return self.desc[:200]

    def date_created_pretty(self):
        return self.date_created.strftime('%b %e %Y')
    
class Question_Survey(models.Model):
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now)

    def date_created_pretty(self):
        return self.date_created.strftime('%b %e %Y')
        
    def __str__(self):
        return "question_"+str(self.id)