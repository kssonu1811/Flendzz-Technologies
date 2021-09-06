from flendzz import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('details/<int:pk>/', views.details, name="details"),
    path('update/<int:pk>/', views.update, name="update"),
    path('deleteorder/<int:pk>/', views.deleteorder, name="deleteorder"),
    path('add/', views.add, name="add"),
]