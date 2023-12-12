from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.accounts.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now)

    groups = None
    user_permissions = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "accounts_user"

    def __str__(self) -> str:
        return self.nip
    
class UserCourse(models.Model):
    id_user = models.IntegerField()
    id_user = models.IntegerField()
    

class Course(models.Model):
    course = models.CharField(max_length=255)
    mentor = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="users", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")
        db_table = "accounts_course"