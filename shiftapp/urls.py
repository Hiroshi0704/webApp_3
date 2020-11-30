from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('shifts', views.ShiftViewSet, 'shifts')
router.register('shiftApps', views.ShiftAppViewSet, 'shiftApps')
router.register(
    'shiftAppWorkerInvitations',
    views.ShiftAppWorkerInvitationViewSet,
    'shiftAppWorkerInvitations')
router.register('workers', views.WorkerViewSet, 'workers')
router.register('shiftPlans', views.ShiftPlanViewSet, 'shiftPlans')
router.register('workPlans', views.WorkPlanViewSet, 'workPlans')
router.register('workSchedules', views.WorkScheduleViewSet, 'workSchedules')
router.register('workStyles', views.WorkStyleViewSet, 'workStyles')

app_name = 'shiftapp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('rest/v1/', include(router.urls)),
]
