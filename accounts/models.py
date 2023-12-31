import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager
from django.core import validators
from django.conf import settings


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField('Nome', max_length=100)
    lastname = models.CharField('Sobrenome', max_length=100)
    name = models.CharField('Nome', max_length=100,blank=True)
    username = models.CharField('Username', max_length=30, unique=True)
    email = models.EmailField('E-mail', unique=True)
    is_active = models.BooleanField('Esta ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =  ['email']

    def __str__(self):
        return self.firstname or self.username

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return str(self)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class PasswordReset(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE, related_name='resets')
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)
    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)
    
    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at']
