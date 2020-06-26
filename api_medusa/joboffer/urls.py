from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobOfferList.as_view()),
    path('tag/', views.TagXJOList.as_view()),
    path('postulation/', views.PostulationList.as_view()),
    path('postulation/select/', views.SelectPostulant.as_view()),
    path('postulation/accept/', views.AcceptPostulant.as_view()),
    path('chat/', views.ChatList.as_view()),
    path('chat/message/', views.MessageList.as_view()),
    path('match/', views.JobMatchList.as_view()),
]
