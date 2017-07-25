"""account urls."""
from extensions.utils import generate_urlpatterns

from account import views


URLS = [
    ('^$', views.HomePageView),
]

# pylint: disable=C0103
urlpatterns = generate_urlpatterns(URLS)
