from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_check),
    path('todos/', views.todos),
    path('todos/<int:id>', views.todos),
]
