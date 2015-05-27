# coding=utf-8
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class StallUserManager(BaseUserManager):
    def create_seller(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class BaseSeller(AbstractBaseUser):
    class Meta:
        app_label = "stall"
        abstract = True

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    validated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    circle_name = models.CharField(max_length=40, help_text="社团名")
    circle_description = models.TextField(help_text="社团介绍")
    circle_image = models.ImageField(upload_to="circle")


    objects = StallUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['circle_name']
