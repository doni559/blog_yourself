# Generated by Django 4.2.7 on 2023-12-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='user',
            field=models.CharField(default='', max_length=50, verbose_name='Пользователь'),
        ),
    ]
