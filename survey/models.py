from django.db import models

class Survey_Templates(models.Model):
    name = models.CharField(max_length=20)
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
    