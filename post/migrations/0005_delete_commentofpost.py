# Generated by Django 5.1.1 on 2024-10-11 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_commentofpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='commentOfpost',
        ),
    ]
