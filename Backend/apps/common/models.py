# common/models.py
from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    """所有业务表的公共审计字段基类"""

    # 创建人
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created",
        help_text="创建人",
    )
    # 创建时间
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, help_text="创建时间"
    )
    # 更新人
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        help_text="更新人",
    )
    # 更新时间
    updated_at = models.DateTimeField(
        auto_now=True, db_index=True, help_text="更新时间"
    )
    # 软删除标记
    is_deleted = models.BooleanField(default=False, db_index=True, help_text="逻辑删除")
    # 乐观锁（行级并发控制）
    version = models.PositiveIntegerField(default=0, help_text="乐观锁版本号")
    # 任意 JSON 扩展字段
    extjson = models.JSONField(default=dict, blank=True, help_text="扩展字段")

    class Meta:
        abstract = True


class HistoryBase(BaseModel):
    object_id = models.UUIDField()  # 主表主键
    snapshot = models.JSONField()  # 当时整行快照（可选）
    diff = models.JSONField(default=dict)  # 字段级变更 diff
    action = models.CharField(max_length=32)  # create / update / delete
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True
    )

    class Meta:
        abstract = True