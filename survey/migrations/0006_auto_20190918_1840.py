# Generated by Django 2.2.5 on 2019-09-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_question_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey_templates',
            name='name',
            field=models.CharField(choices=[('Question_Survey', 'Question_Survey')], default='Question_Survey', max_length=20),
        ),
    ]
