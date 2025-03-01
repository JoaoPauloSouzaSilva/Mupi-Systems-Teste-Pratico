from django.urls import path, include # type: ignore
from django.contrib.auth.views import LogoutView # type: ignore
from django.contrib import messages # type: ignore
from django.shortcuts import redirect # type: ignore
from tasks import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('login')),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),  
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/complete/', views.task_mark_complete, name='task_mark_complete'),
    path('unmark/<int:pk>/', views.task_unmark_complete, name='task_unmark_complete'),
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
]
