# Generated by Django 4.2.11 on 2024-03-19 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='author_id',
        ),
    ]
