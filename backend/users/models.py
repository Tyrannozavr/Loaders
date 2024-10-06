from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)




class User(AbstractUser):
    email = models.EmailField(db_index=True, unique=True, max_length=254, verbose_name='Электронная почта')
    surname = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Отчество")
    first_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Фамилия')
    username = models.CharField(max_length=1000, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):
        last_name = self.last_name if self.last_name else ''
        first_name = self.first_name if self.first_name else ''
        surname = self.surname if self.surname else ''
        return f'{last_name} {first_name} {surname}'

    @property
    def full_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()