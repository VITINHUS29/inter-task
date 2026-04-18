from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    path('tasks/', views.task_list, name='tasks'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/delete/<int:id>/', views.task_delete, name='task_delete'),

    path('kanban/', views.kanban_view, name='kanban'),
    
    path('task/change-status/<int:task_id>/<str:new_status>/', views.change_status, name='change_status'),
    
    path('calendar/', views.calendar_view, name='calendar'),
    
    path('profile/', views.profile_view, name='profile'),
]