from django.contrib.auth.models import User
from django.db import models
from PIL import Image

CHOICES = (('b', "+18"), ('s', '-18'))
TYPE = (
    ('full', 'Полный пакет'),
    ('free', 'Бесплатный пакет')
)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    adult = models.CharField('Пол пользователя ', choices=CHOICES, max_length=15, default='m')
    subscription = models.BooleanField(verbose_name='Подписка', default=True, blank=False)
    account_type = models.CharField(choices=TYPE, default='free', max_length=100)

    def __str__(self):
        return f" {self.user.username}"


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
