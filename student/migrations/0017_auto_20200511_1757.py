# Generated by Django 3.0.5 on 2020-05-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_notes_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
