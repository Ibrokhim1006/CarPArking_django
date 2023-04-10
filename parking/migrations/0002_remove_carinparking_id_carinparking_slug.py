# Generated by Django 4.2 on 2023-04-09 06:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carinparking',
            name='id',
        ),
        migrations.AddField(
            model_name='carinparking',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]