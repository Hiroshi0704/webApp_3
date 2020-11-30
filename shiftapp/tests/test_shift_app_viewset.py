from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.test.utils import override_settings
from django.conf import settings
from rest_framework.test import APITestCase

from shiftapp.models import ShiftAppPlan, ShiftApp
from .utils import TestUtilMixin


@override_settings(
    LANGUAGE_CODE='EN',
    INSTALLED_APPS=[app for app in settings.INSTALLED_APPS if app != 'debug_toolbar'],
    MIDDLEWARE=[mdwer for mdwer in settings.MIDDLEWARE if mdwer != 'debug_toolbar.middleware.DebugToolbarMiddleware'],
)
class TestShiftAppViewSet(APITestCase, TestUtilMixin):

    TARGET_URL = '/shiftApp/rest/v1/shiftApps/'

    def setUp(self):
        self.testuser000 = self._insert_user(email='testuser000@example.com')
        self.testuser001 = self._insert_user(email='testuser001@example.com')

        self.shiftAppPlanFree = ShiftAppPlan.objects.create(
            title='Free',
            price=0,
            is_manager=False,
            max_worker=0)

        self.shiftAppPlanMax5 = ShiftAppPlan.objects.create(
            title='Plan1',
            price=100,
            is_manager=True,
            max_worker=5)

    def test_get_by_unauthenticated_user(self):
        resp = self.client.get(self.TARGET_URL)
        self.assertEqual(resp.status_code, 403)

    def test_get_by_authenticated_user(self):
        self._login(
            self.testuser000.email,
            self.testuser000.row_password)
        resp = self.client.get(self.TARGET_URL)
        self.assertEqual(resp.status_code, 200)
        expected_json = []
        self.assertJSONEqual(resp.content, expected_json)

    def test_post_by_unauthenticated_user(self):
        params = {
            'user': str(self.testuser000.id),
            'plan': str(self.shiftAppPlanFree.id)
        }
        resp = self.client.post(self.TARGET_URL, params, format='json')
        self.assertEqual(resp.status_code, 403)

    def test_post_by_authenticated_user(self):
        self._login(
            self.testuser000.email,
            self.testuser000.row_password)
        params = {
            'user': str(self.testuser000.id),
            'plan': str(self.shiftAppPlanFree.id)
        }
        resp = self.client.post(self.TARGET_URL, params, format='json')
        self.assertEqual(resp.status_code, 201)

    def test_complete_new_registration(self):
        self._login(
            self.testuser000.email,
            self.testuser000.row_password)
        params = {
            'user': str(self.testuser000.id),
            'plan': str(self.shiftAppPlanFree.id)
        }
        resp = self.client.post(self.TARGET_URL, params, format='json')
        shiftApp = ShiftApp.objects.filter(user=self.testuser000)
        self.assertEqual(shiftApp.count(), 1)

        shiftApp = shiftApp.first()
        expected_json = {
            'id': str(shiftApp.id),
            'user': str(shiftApp.user.id),
            'plan': str(shiftApp.plan.id),
            'plan_info': {
                'is_manager': shiftApp.plan.is_manager,
                'max_worker': shiftApp.plan.max_worker,
                'price': shiftApp.plan.price,
                'title': shiftApp.plan.title,
            },
        }
        self.assertJSONEqual(resp.content, expected_json)

    def test_new_registration_again_by_same_user(self):
        self._login(
            self.testuser000.email,
            self.testuser000.row_password)
        params = {
            'user': str(self.testuser000.id),
            'plan': str(self.shiftAppPlanFree.id)
        }
        resp = self.client.post(self.TARGET_URL, params, format='json')
        self.assertEqual(resp.status_code, 201)
        shiftApp = ShiftApp.objects.filter(user=self.testuser000)
        self.assertEqual(shiftApp.count(), 1)

        params['plan'] = str(self.shiftAppPlanMax5.id)
        error_msg = 'UNIQUE constraint failed: shiftapp_shiftapp.user_id'
        with self.assertRaisesMessage(IntegrityError, error_msg):
            resp = self.client.post(self.TARGET_URL, params, format='json')

    def test_update_plan(self):
        self._login(self.testuser000.email, self.testuser000.row_password)
        params = {
            'user': str(self.testuser000.id),
            'plan': str(self.shiftAppPlanFree.id)
        }
        self.client.post(self.TARGET_URL, params, format='json')
        params['plan'] = str(self.shiftAppPlanMax5.id)
        app = ShiftApp.objects.get(user=self.testuser000)
        resp = self.client.put(self.TARGET_URL + str(app.id) + '/', params)
        self.assertEqual(resp.status_code, 200)
        newapp = ShiftApp.objects.get(user=self.testuser000)
        self.assertEqual(newapp.plan.id, self.shiftAppPlanMax5.id)
        self.assertNotEqual(newapp.plan.id, app.plan.id)

    def test_update_user(self):
        self._login(self.testuser000.email, self.testuser000.row_password)
        params = {
            'user': str(self.testuser000.id),
            'plan': str(self.shiftAppPlanFree.id)
        }
        self.client.post(self.TARGET_URL, params, format='json')

        params['user'] = str(self.testuser001.id)
        app = ShiftApp.objects.get(user=self.testuser000)
        resp = self.client.put(self.TARGET_URL + str(app.id) + '/', params)
        expected_json = {
            'id': str(app.id),
            'user': str(self.testuser000.id),
            'plan': str(self.shiftAppPlanFree.id),
            'plan_info': {
                'is_manager': app.plan.is_manager,
                'max_worker': app.plan.max_worker,
                'price': app.plan.price,
                'title': app.plan.title,
            },
        }
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, expected_json)
        with self.assertRaises(ObjectDoesNotExist):
            ShiftApp.objects.get(user=self.testuser001)
