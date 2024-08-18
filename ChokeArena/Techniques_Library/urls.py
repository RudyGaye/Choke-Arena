from django.urls import path
from . import views

urlpatterns = [
    # Base URL to access the techniques library
    path('', views.techniques_library, name='techniques_library'),

    # URL to add a new technique
    path('add_technique/', views.add_technique, name='add_technique'),

    # URL to view details of a specific technique
    path('technique/<int:technique_id>/', views.technique_detail, name='technique_detail'),

    # URL to view details of a specific category
    path('category/<int:id>/', views.category_detail, name='category_detail'),

    # URL to view details of a specific technique type
    path('type/<int:id>/', views.type_detail, name='type_detail'),

    # URL to follow a specific technique
    path('<int:technique_id>/follow/', views.follow_technique, name='follow_technique'),

    # URL to unfollow a specific technique
    path('<int:technique_id>/unfollow/', views.unfollow_technique, name='unfollow_technique'),
]
