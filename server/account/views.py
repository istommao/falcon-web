"""account views."""
from django.views import generic


class HomePageView(generic.TemplateView):
    """Collect listview."""

    view_name = 'homepage'

    template_name = 'index.html'
