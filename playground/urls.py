from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_check),
    path('todos/', views.todos),
]
