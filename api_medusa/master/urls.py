from django.urls import path
from . import views

urlpatterns = [
    path('facultad/', views.FacultadList.as_view()),
    path('escuela/', views.EscuelaList.as_view()),
    path('tag/', views.TagList.as_view()),
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('collaborator/', views.CollaboratorList.as_view()),
    path('collaborator/tag/', views.TagXCollaboratorList.as_view()),
]
