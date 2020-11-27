from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('shifts', views.ShiftViewSet, 'shifts')
router.register('shiftApps', views.ShiftAppViewSet, 'shiftApps')

app_name = 'shiftApp'
urlpatterns = [
    path('rest/', include(router.urls)),
]
