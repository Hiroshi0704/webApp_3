from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View
from django.shortcuts import get_object_or_404, render

from shiftapp.models import ShiftApp


class HomeView(LoginRequiredMixin, UserPassesTestMixin, View):
    """勤務表作成機能ホーム画面"""

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'shiftapp/home.html', context)

    def test_func(self):
        app = get_object_or_404(ShiftApp, user=self.request.user)
        return app.user.id == self.request.user.id
