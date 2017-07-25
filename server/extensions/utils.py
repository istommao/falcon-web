"""extensions utils."""
from django.conf.urls import url


def generate_urlpatterns(urls):
    """Generate urlpatterns."""
    patterns = [url(pattern, view.as_view(),
                    name=view.view_name) for pattern, view in urls]

    return patterns
