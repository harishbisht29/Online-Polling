# Generated by Django 2.2.5 on 2019-09-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey_Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=1000)),
                ('thumbnail', models.ImageField(upload_to='images/')),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]