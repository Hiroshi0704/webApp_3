from django.test import TestCase
from django.contrib.auth import get_user_model, get_user
from django.urls import reverse
from django.conf import settings
from django.test.utils import override_settings
from django.test.client import Client

from .admin import CustomUserCreationForm
from .models import User


@override_settings(
    LANGUAGE_CODE='EN',
    INSTALLED_APPS=[l for l in settings.INSTALLED_APPS if l != 'debug_toolbar'],
    MIDDLEWARE=[l for l in settings.MIDDLEWARE if l != 'debug_toolbar.middleware.DebugToolbarMiddleware'],
)
class AccountTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='Password01')

        self.superUser = get_user_model().objects.create_superuser(
            email='super@example.com',
            password='Password01')

    def test_login_exists_user(self):
        self.assertNotIn('_auth_user_id', self.client.session)
        resp = self.client.post(
            reverse('account_login'),
            {'login': 'testuser@example.com', 'password': 'Password01'}
        )
        self.assertRedirects(resp, reverse('index'))
        self.assertIn('_auth_user_id', self.client.session)
        self.assertEqual(
            self.client.session['_auth_user_id'], str(self.user.pk))

    def test_login_not_exists_user(self):
        resp = self.client.post(
            reverse('account_login'),
            {'login': 'bad@example.com', 'password': 'bad'}
        )
        self.assertFormError(
            resp,
            'form',
            None,
            'The e-mail address and/or password you specified are not correct.'
        )

    def test_login_page_with_logged_in(self):
        client = Client()
        client.force_login(self.user)
        resp = client.get(reverse('account_login'))
        self.assertRedirects(resp, reverse('index'))
        self.assertTemplateUsed('account/login.html')

    def test_logout_page_with_logged_in(self):
        client = Client()
        client.force_login(self.user)
        resp = client.get(reverse('account_logout'))
        self.assertTemplateUsed('account/logout.html')
        self.assertEqual(resp.status_code, 200)

    def test_logout(self):
        client = Client()
        client.force_login(self.user)
        self.assertIn('_auth_user_id', client.session)
        self.assertEqual(client.session['_auth_user_id'], str(self.user.pk))

        resp = client.post(reverse('account_logout'))
        self.assertRedirects(resp, reverse('account_login'))
        self.assertTrue(self.user.is_authenticated)
        self.assertNotIn('_auth_user_id', client.session)

    def test_logout_page_with_not_logged_in(self):
        resp = self.client.get(reverse('account_logout'))
        self.assertRedirects(resp, reverse('account_login'))

    def test_login_failed_attemps_exceeded(self):
        for i in range(7):
            is_valid_attempt = (i == 6)
            is_locked = (i >= 5)
            resp = self.client.post(
                reverse('account_login'),
                {
                    'login': self.user.email,
                    'password': (self.user.password if is_valid_attempt else 'bad')
                }
            )
            error_msg_1 = 'Too many failed login attempts. Try again later.'
            error_msg_2 = 'The e-mail address and/or password you specified are not correct.'
            self.assertFormError(
                resp,
                "form",
                None,
                error_msg_1 if is_locked else error_msg_2,
            )

    def test_create_user_at_admin_page(self):
        client = Client()
        client.force_login(self.superUser)
        resp = client.get('/admin/accounts/user/add/')
        self.assertEqual(resp.status_code, 200)

        resp = client.post('/admin/accounts/user/add/', {
            'email': 'newuser@example.com',
            'password': 'adfaoiie001',
            'is_active': 'on',
            'date_joined_0': '2020-11-22',
            'date_joined_1': '11:42:25',
            'initial-date_joined_0': '2020-11-22',
            'initial-date_joined_1': '11:42:25',
            '_save': 'save',
            '_continue': 1
        })
        user = User.objects.get(email='newuser@example.com')
        self.assertRedirects(
            resp,
            '/admin/accounts/user/' + str(user.id) + '/change/')

    def test_create_user_form_common_password(self):
        data = {
            'email': 'newuser@example.com',
            'password': 'password',
            'is_active': 'on',
            'date_joined_0': '2020-11-22',
            'date_joined_1': '11:42:25',
            'initial-date_joined_0': '2020-11-22',
            'initial-date_joined_1': '11:42:25',
            '_save': 'save',
            '_continue': 1
        }
        form = CustomUserCreationForm(data)
        form.is_valid()
        self.assertTrue(
            'This password is too common.' in form.errors['password'])

    def test_create_user_form_save(self):
        data = {
            'email': 'newuser@example.com',
            'password': 'adfaiita011',
            'is_active': 'on',
            'date_joined_0': '2020-11-22',
            'date_joined_1': '11:42:25',
            'initial-date_joined_0': '2020-11-22',
            'initial-date_joined_1': '11:42:25',
            '_save': 'save',
            '_continue': 1
        }
        form = CustomUserCreationForm(data)
        if form.is_valid():
            form.save()

        newUser = User.objects.get(email=data['email'])
        self.assertEqual(data['email'], newUser.email)

    def test_create_user_email_empty(self):
        with self.assertRaisesMessage(
                ValueError, 'The given email must be set'):
            User.objects.create_user(email=None)

    def test_create_superuser_is_staff_false(self):
        with self.assertRaisesMessage(
                ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                email='newsuper@example',
                password='amdfoaijgllwoijAADF001',
                is_staff=False)

    def test_create_superuser_is_superuser_false(self):
        with self.assertRaisesMessage(
                ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                email='newsuper@example',
                password='amdfoaijgllwoijAADF001',
                is_superuser=False)
