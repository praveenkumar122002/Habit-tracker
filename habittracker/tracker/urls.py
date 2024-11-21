from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views  # Assuming 'views' has your register view

urlpatterns = [
    # Habit Tracker URLs
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_habit, name='add_habit'),
    path('edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('mark_complete/<int:habit_id>/', views.mark_complete, name='mark_complete'),
    path('update_status/<int:habit_id>/<str:new_status>/', views.update_status, name='update_status'),
    path('logout/',views.custom_logout_view,name='logout'),
    
    # Authentication URLs
    path('register/', views.register, name='register'),  # Registration page (make sure you have the register view)
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]


