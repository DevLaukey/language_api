# Generated by Django 5.0.4 on 2024-04-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisequestion',
            name='correct_choice',
        ),
        migrations.AddField(
            model_name='questionchoice',
            name='correct_choice',
            field=models.BooleanField(default=False),
        ),
    ]
