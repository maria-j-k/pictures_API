# Generated by Django 3.2.4 on 2021-06-23 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210622_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnail',
            name='valid',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
