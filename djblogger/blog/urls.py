from django.contrib import admin
from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
    )

urlpatterns = [
    # path('', views.home, name='home'),
    path('', PostListView.as_view(), name='home'),
    # path('delete-view', PostdeleteView.as_view(), name='delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('technical/', views.technical_post, name='technical'),
    path('exercise/', views.technical_ex, name='exercise'),
    path('structure/', views.database_hand, name='structure'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete')
]
