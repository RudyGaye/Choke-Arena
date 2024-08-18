# Community/urls.py
from django.urls import path
from .views import forum_list, topic_list, topic_detail, new_topic, edit_topic, delete_topic, edit_post, delete_post

urlpatterns = [
    path('forums/', forum_list, name='forum_list'),
    path('forums/<int:forum_id>/topics/', topic_list, name='topic_list'),
    path('topics/<int:topic_id>/', topic_detail, name='topic_detail'),
    path('forums/<int:forum_id>/topics/new/', new_topic, name='new_topic'),
    path('topics/<int:topic_id>/edit/', edit_topic, name='edit_topic'),
    path('topics/<int:topic_id>/delete/', delete_topic, name='delete_topic'),
    path('posts/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),
]
