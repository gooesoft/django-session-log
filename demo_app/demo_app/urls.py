from django.conf.urls import url, include
from django.contrib import admin

from session_activity import urls as session_urls
from simple_login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^login/$", views.SimpleLogin.as_view()),
    url(r"^", include(session_urls)),
]
