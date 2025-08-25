# apps/identity/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.common.models import BaseModel


class Role(BaseModel):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser, BaseModel):
    phone = models.CharField(max_length=11, unique=True)
    avatar = models.URLField(blank=True)

    roles = models.ManyToManyField(
        Role,
        through='UserRole',
        blank=True
    )
    # 仅做快速 UI 判断，Casbin 仍是唯一权威
    is_super_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'rbac_user'
        swappable = 'AUTH_USER_MODEL'


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'rbac_user_role'
        unique_together = ('user', 'role')