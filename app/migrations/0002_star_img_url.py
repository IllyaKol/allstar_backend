# Generated by Django 3.0.4 on 2020-03-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='img_url',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
