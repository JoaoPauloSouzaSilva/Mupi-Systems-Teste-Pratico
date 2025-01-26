from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views # type: ignore
from tasks.forms import CustomLoginForm # type: ignore

urlpatterns = [
    path(
        '',
        auth_views.LoginView.as_view(
            template_name='tasks/login.html',
            authentication_form=CustomLoginForm
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
