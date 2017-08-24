"""falcon urls."""
"""info urls module."""
from extensions.utils import generate_urlpatterns

from falcon import views

URLS = [
    ('^$', views.IndexView),
    ('^login/$', views.LoginPageView)
]

# pylint: disable=C0103
urlpatterns = generate_urlpatterns(URLS)
