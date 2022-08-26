from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('comments/',views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view()),
    
]
