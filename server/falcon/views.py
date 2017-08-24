"""falcon views."""
from __future__ import print_function

from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import redirect


class IndexView(generic.TemplateView):
    """IndexView"""

    view_name = 'index'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class LoginPageView(generic.TemplateView):
    """LoginPageView"""

    view_name = 'login'
    template_name = 'login.html'

    def post(self, request):
        """Post."""
        return redirect(reverse('falcon:index'))
