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

    roles = models.ManyToManyField(Role, through="UserRole", blank=True)

    # 复用 Django 内置字段
    # is_superuser 默认存在，不覆盖即可
    # is_staff 如需要后台登录，也保留

    class Meta:
        db_table = "rbac_user"
        swappable = "AUTH_USER_MODEL"


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "rbac_user_role"
        unique_together = ("user", "role")
