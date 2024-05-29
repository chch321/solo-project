from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("username을 입력해주세요")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(username=username, password=password)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user.is_admin = True
        user.save()
        return user

    
class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(("first name"), max_length=150, blank=True)
    last_name = models.CharField(("last name"), max_length=150, blank=True)
    email = models.EmailField(("email address"), blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='ozusers_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='ozusers_permissions', 
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

