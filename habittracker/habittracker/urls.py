from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView,LogoutView
from tracker import views  # Ensure this import is correct
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Default authentication URLs (login, logout, password change, etc.)
    path('accounts/', include('django.contrib.auth.urls')),  # This includes login, logout, etc.
    
    # Habit Tracker URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('add/', views.add_habit, name='add_habit'),
    path('edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('complete/<int:habit_id>/', views.mark_complete, name='mark_complete'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('update_status/<int:habit_id>/<str:new_status>/', views.update_status, name='update_status'),
    
    
    # Authentication URLs
    path('register/', views.register, name='register'),  # Registration page (ensure you have a 'register' view)
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Root URL redirects to login page
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
]


