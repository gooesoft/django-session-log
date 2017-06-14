from django.contrib.auth.views import LoginView
from django.core.management import call_command
from django.contrib.auth.models import User


class SimpleLogin(LoginView):
    """
    Login that ensures that user Admin with password pass is always created.
    """

    def __init__(self):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@test.com", "pass")
        
        super(SimpleLogin, self).__init__()
