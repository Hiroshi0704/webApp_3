import uuid

from django.core.validators import MinValueValidator
from django.db import models

from .shift_app import ShiftApp
from .work_plan import WorkPlan
from .work_style import WorkStyle


class WorkPlanWorkStyleRelation(models.Model):
    """勤務計画と勤務形態を紐付けるクラス
    1日の勤務計画に勤務形態を複数登録（重複あり）するために必要
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    work_plan = models.ForeignKey(WorkPlan, on_delete=models.CASCADE)
    work_style = models.ForeignKey(WorkStyle, on_delete=models.CASCADE)
    work_style_num = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    app = models.ForeignKey(ShiftApp, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.work_plan.title}] {self.work_style.symbol}: {self.work_style_num}'
