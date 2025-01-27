from django.urls import path, include # type: ignore
from django.contrib.auth.views import LogoutView # type: ignore
from tasks import views
from django.shortcuts import redirect # type: ignore

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('login')),

    path('home/', views.home, name='home'),  # Adiciona a página inicial
    
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
     path('<int:pk>/complete/', views.task_mark_complete, name='task_mark_complete'),

     # Logout configurado para aceitar métodos GET
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
]
