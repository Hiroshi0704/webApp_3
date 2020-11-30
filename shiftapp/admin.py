from django.contrib import admin

from .models import (Shift, ShiftApp, ShiftAppPlan, ShiftPlan,
                     ShiftWorkerRelation, Worker, WorkPlan,
                     WorkPlanWorkStyleRelation, WorkSchedule, WorkStyle,
                     ShiftAppWorkerInvitation)

admin.site.register(Shift)
admin.site.register(ShiftApp)
admin.site.register(ShiftAppPlan)
admin.site.register(ShiftPlan)
admin.site.register(ShiftWorkerRelation)
admin.site.register(Worker)
admin.site.register(WorkPlan)
admin.site.register(WorkPlanWorkStyleRelation)
admin.site.register(WorkSchedule)
admin.site.register(WorkStyle)
admin.site.register(ShiftAppWorkerInvitation)
