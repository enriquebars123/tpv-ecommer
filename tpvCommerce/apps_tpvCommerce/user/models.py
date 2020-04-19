""" Modelo de Usuario """

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils import timezone

# Django
from django.db import models
from django.contrib.auth.models import User
#from decouple import config


class userManager(BaseUserManager):
    def create_user(
        self,
        username,
        email,
        name,
        password=None
    ):
        if not email:
            raise ValueError('Campo de Correo Obligatorio')

        user_obj = self.model(
            username=username,
            email=email,
            name=name,
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(
        self,
        username,
        email,
        name,
        password
    ):
        usuario_obj = self.create_user(
            username=username,
            email=email,
            name=name,
        )
        usuario_obj.is_superuser = True
        usuario_obj.is_active = True
        usuario_obj.is_staff = True
        usuario_obj.set_password(password)
        usuario_obj.save(using=self._db)
        return usuario_obj


class user(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    name = models.CharField(max_length=250)
    is_active  = models.BooleanField(default=False,)
    is_staff = models.BooleanField(default=False,)
    is_superuser = models.BooleanField(default=True,)
   

    objects = userManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'name',
        'email',
    ]

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class people(models.Model):
    user = models.ForeignKey( user , on_delete=models.CASCADE, null=False,blank= False )
    nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    lastname = models.CharField(max_length=50)
    street = models.CharField(max_length=250, null=True, blank=True)
    colony = models.CharField(max_length=250, null=True, blank=True)
    postalCode = models.CharField(max_length=5, null=True, blank=True)
    cellPhone = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=10,null=True, blank=True)

    class Meta:
        db_table = 'people'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

