from django.contrib.auth import get_user_model


class TestUtilMixin:

    def _login(self, email, password):
        self.assertNotIn('_auth_user_id', self.client.session)
        self.client.login(
            username=email,
            password=password)
        self.assertIn('_auth_user_id', self.client.session)

    def _get_dummy_password(self):
        return 'TestPass01'

    def _insert_user(self, email, password=None):
        if password is None:
            password = self._get_dummy_password()
        user = get_user_model().objects.create_user(
            email=email,
            password=password)
        user.row_password = password
        return user
