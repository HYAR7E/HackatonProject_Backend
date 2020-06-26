from rest_framework import generics
from .serializers import *
from .models import *


class FacultadList(generics.ListCreateAPIView):
    """
    GET: List all Facultad registers
    POST: Create a new Facultad register
    """
    serializer_class = FacultadSz
    queryset = Facultad.objects.all()


class EscuelaList(generics.ListCreateAPIView):
    """
    GET: List all Escuela registers
    POST: Create a new Escuela register
    """
    serializer_class = EscuelaSz
    queryset = Escuela.objects.all()


class TagList(generics.ListCreateAPIView):
    """
    GET: List all Tag registers
    POST: Create a new Tag register
    """
    serializer_class = TagSz
    queryset = Tag.objects.all()


class UserList(generics.ListCreateAPIView):
    """
    GET: List all User registers
    POST: Create a new User register
    """
    serializer_class = UserSz
    queryset = User.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """ GET - UPDATE - DESTROY """
    serializer_class = UserSz
    queryset = User.objects.all()


class CollaboratorList(generics.ListCreateAPIView):
    """
    GET: List all Collaborator registers
    POST: Create a new Collaborator register
    """
    serializer_class = CollaboratorSz
    queryset = Collaborator.objects.all()


class TagXCollaboratorList(generics.ListCreateAPIView):
    """
    GET: List all Collaborator's Tags
    POST: Add a Tag to Collaborator
    """
    serializer_class = TagXCollaboratorSz
    queryset = TagXCollaborator.objects.all()
