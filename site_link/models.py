from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Links(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь ', on_delete=models.CASCADE)
    slug = models.CharField('Уникальное название ', unique=True, max_length=30)
    link = models.CharField('Ссылка', max_length=999)

    def __str__(self):
        return self.slug
