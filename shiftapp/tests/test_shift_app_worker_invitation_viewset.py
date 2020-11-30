from django.db import IntegrityError
from django.test.utils import override_settings
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from shiftapp.models import ShiftAppPlan, ShiftApp
from .utils import TestUtilMixin


@override_settings(
    LANGUAGE_CODE='EN',
    INSTALLED_APPS=[app for app in settings.INSTALLED_APPS if app != 'debug_toolbar'],
    MIDDLEWARE=[mdwer for mdwer in settings.MIDDLEWARE if mdwer != 'debug_toolbar.middleware.DebugToolbarMiddleware'],
)
class TestShiftAppWorkerInvitationViewSet(APITestCase, TestUtilMixin):

    TARGET_URL = '/shiftApp/rest/v1/shiftAppWorkerInvitations/'

    def setUp(self):
        self.testuser = self._insert_user(email='testuser@example.com')
        self.app_user = self._insert_user(email='app_user@example.com')

        self.free_plan = ShiftAppPlan.objects.create(
            title='Free',
            is_manager=False,
            price=0.0,
            max_worker=0)

        ShiftApp.objects.create(
            user=self.app_user,
            plan=self.free_plan)

    def test_get_by_unauthenticated_user(self):
        resp = self.client.get(self.TARGET_URL)
        self.assertEqual(resp.status_code, 403)

    def test_get_by_authenticated_user_before_registering_shiftApp(self):
        self._login(self.testuser.email, self.testuser.row_password)
        resp = self.client.get(self.TARGET_URL)
        self.assertEqual(resp.status_code, 404)
        expected_json = {'detail': 'Not found.'}
        self.assertJSONEqual(resp.content, expected_json)

    def test_get_by_authenticated_user_after_registering_shiftApp(self):
        self._login(self.app_user.email, self.app_user.row_password)
        resp = self.client.get(self.TARGET_URL)
        self.assertEqual(resp.status_code, 200)
        expected_json = []
        self.assertJSONEqual(resp.content, expected_json)
