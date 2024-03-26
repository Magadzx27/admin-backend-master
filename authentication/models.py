from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):

    def create_user(
        self,
        username,
        email,
        picture=None,
        password=None,
        name=None,
        phone=None,
        address=None,
        country=None,
        zip_code=None,
        dob=None
    ):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TabError('Users should have a email')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            picture=picture,
            phone=phone,
            address=address,
            country=country
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError('Password should not be None')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_manager = True
        user.save()
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=False, blank=False)
    phone = PhoneNumberField(null=True, blank=True)
    username = models.CharField(max_length=500, unique=True, db_index=True)
    email = models.EmailField(max_length=500, unique=True, db_index=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    picture = models.URLField(max_length=1000, blank=True, null=True)
    dob = models.DateTimeField(blank=True,null=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_manager = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
