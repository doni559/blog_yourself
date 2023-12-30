from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(verbose_name='Название',max_length=50, default = '')
    anounce = models.CharField(verbose_name='Анонс', max_length=255)
    full_text = models.TextField(verbose_name='Статья')
    user=models.CharField(verbose_name='Пользователь', max_length=50, default='')
    date= models.DateField(verbose_name='Дата публикации')

    def __str__(self):
        return f'Новость: {self.title}'

        
    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'