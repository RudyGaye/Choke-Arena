from django.urls import path
from . import views
from .views import signup
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Route for the login page, uses a custom view
    path('login/', views.login, name='login'),

    # Route for logging out, redirects to 'home_index' after logout
    path('logout/', LogoutView.as_view(next_page='home_index'), name='logout'),

    # Route for the profile page, uses a custom view
    path('profil/', views.profil, name='profil'),

    # Route for user signup, uses a custom view
    path('signup/', signup, name='signup'),

    # Routes for password reset functionality, using built-in Django views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Route for viewing items followed by the user, uses a custom view
    path('my-followed-items/', views.user_followed_items, name='user_followed_items'),
]

# Optional: Add static and media URL patterns if your project is serving static files or media files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
