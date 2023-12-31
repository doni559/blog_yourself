# Generated by Django 4.2.7 on 2023-12-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allusersdata',
            name='user',
        ),
        migrations.AddField(
            model_name='allusersdata',
            name='username',
            field=models.CharField(default='', max_length=50, verbose_name='Никнейм'),
        ),
        migrations.AlterField(
            model_name='allusersdata',
            name='about',
            field=models.TextField(default='', verbose_name='Обо мне'),
        ),
        migrations.AlterField(
            model_name='allusersdata',
            name='status',
            field=models.CharField(default='', max_length=20, verbose_name='Статус'),
        ),
    ]
