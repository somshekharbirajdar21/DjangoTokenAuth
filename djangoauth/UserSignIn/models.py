from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, MobileNumber, password=None, **extra_fields):
        """
        Creates and saves a User with the given mobile number and password.
        """
        if not MobileNumber:
            raise ValueError('The mobile number field must be set')
        user = self.model(MobileNumber=MobileNumber, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, MobileNumber, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given mobile number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(MobileNumber, password, **extra_fields)

    def get_by_natural_key(self, MobileNumber):
        """
        Return the user with the given MobileNumber.
        """
        return self.get(MobileNumber=MobileNumber)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    firstName =models.CharField(max_length=10, blank=True)
    lastName =models.CharField(max_length=10, blank=True)
    email = models.EmailField()
    MobileNumber = models.CharField(max_length=10, blank=True, unique= True)
    password = models.CharField(max_length=10, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'MobileNumber'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
