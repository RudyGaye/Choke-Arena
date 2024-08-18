"""
URL configuration for Choke_Arena project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# choke_arena/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('User_Management/', include('User_Management.urls')),
    path('', include('Home.urls')),
    path('Techniques_Library/', include('Techniques_Library.urls')),
    path('Training_Plans/', include('Training_Plans.urls')),
    path('Community/', include('Community.urls')),
]