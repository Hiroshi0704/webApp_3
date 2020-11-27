import uuid

from django.core.validators import MinValueValidator
from django.db import models


class ShiftAppPlan(models.Model):
    """勤務表作成機能登録プラン"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, unique=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    is_manager = models.BooleanField(default=True)
    max_worker = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'[{self.title}] {self.price}'
