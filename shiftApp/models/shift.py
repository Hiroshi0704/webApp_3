import datetime
import uuid

from django.db import models

from .shift_app import ShiftApp
from .worker import Worker


class Shift(models.Model):
    """勤務表"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    worker = models.ManyToManyField(Worker)
    is_public = models.BooleanField(default=False)
    app = models.ForeignKey(ShiftApp, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_day_range(self):
        diff = (self.end_date - self.start_date).days
        return [self.start_date + datetime.timedelta(days=i) for i in range(diff + 1)]
