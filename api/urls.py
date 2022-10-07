from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_view),
    path('articles/<int:pk>/', views.article_view),
    path('articles/', views.article_view),
]