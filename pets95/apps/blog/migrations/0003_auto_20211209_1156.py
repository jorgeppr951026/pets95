# Generated by Django 3.1.7 on 2021-12-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='bibliografia',
            field=models.TextField(blank=True, null=True, verbose_name='Referencias Bibliográficas'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Imagen'),
        ),
    ]
