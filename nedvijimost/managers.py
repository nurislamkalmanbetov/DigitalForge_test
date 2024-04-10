import uuid
from django.db import models
from django.db.models import Q
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, is_staff=False, is_superuser=False, **extra_fields):
        if not password:
            raise ValueError('User must have a password.')

        if not email:
            raise ValueError('User must have an email.')

        model_data = {'is_staff': is_staff, 'is_superuser': is_superuser}

        if email:
            model_data['email'] = self.normalize_email(email)

        user = self.model(**model_data, **extra_fields)
        user.set_password(password)  # Здесь пароль захеширован
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)