from django.urls import path
from . import views

urlpatterns = [
    # Index page for training plans
    path('', views.index, name='training_plans_index'),
    
    # List of training plans
    #path('training_plans/', views.training_plans, name='training_plans'),
    
    # Add a new training plan
    path('add/', views.add_training_plan, name='add_training_plan'),
    
    # Detail view of a specific training plan
    path('<int:plan_id>', views.training_plan_detail, name='training_plan_detail'),
    
    # Follow a specific training plan
    path('<int:plan_id>/follow/', views.follow_training_plan, name='follow_training_plan'),
    
    # Unfollow a specific training plan
    path('<int:plan_id>/unfollow/', views.unfollow_training_plan, name='unfollow_training_plan'),
    
    # Search functionality
    path('search/', views.search, name='search'),
]
