# Generated by Django 3.0.7 on 2020-06-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='order',
            field=models.CharField(max_length=3),
        ),
    ]