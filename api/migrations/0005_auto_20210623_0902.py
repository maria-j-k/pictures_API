# Generated by Django 3.2.4 on 2021-06-23 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_thumbnail_valid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thumbnail',
            old_name='created',
            new_name='expires',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='valid',
        ),
    ]
