# Generated by Django 4.1.7 on 2023-04-13 12:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
