from django.urls import path
from . import views

urlpatterns = [
    path('token/login/', views.GenerateToken.as_view()),
    path('token/logout/', views.DeleteToken.as_view()),
]
