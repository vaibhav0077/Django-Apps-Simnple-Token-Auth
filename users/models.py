from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError(_('users must have an email address'))
        email = self.normalize_email(email)

        user = self.model(email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser,

                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

    # def _create_user(self, email, password, **extra_fields):
    #     if not email:
    #         raise ValueError('Users require an email field')
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_user(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(email, password, **extra_fields)

    # def create_superuser(self, email, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)

    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')

    #     return self._create_user(email, password, **extra_fields)


# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(
#         'First Name', max_length=255, blank=True, null=False)
#     last_name = models.CharField(
#         'Last Name', max_length=255, blank=True, null=False)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return f"{self.email} - {self.first_name} {self.last_name}".


class CustomUser( AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str__(self):
        return self.email
