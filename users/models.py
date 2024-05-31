from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {
    'null': True,
    'blank': True,
}


class User(AbstractUser):

    username = None
    first_name = models.CharField(max_length=150, **NULLABLE)
    last_name = models.CharField(max_length=150, **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='Активность')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
