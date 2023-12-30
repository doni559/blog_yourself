from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AllUsersData(models.Model):
    username=models.CharField(verbose_name="Никнейм", max_length=50, default='')
    about=models.TextField(verbose_name="Обо мне", default='')
    status=models.CharField(verbose_name="Статус", max_length=20, default='')

    def __str__(self):
        return f"Пользователь: {self.username}"

    class Meta():
        verbose_name='Информация о пользователе'
        verbose_name_plural='Информация о пользователях'