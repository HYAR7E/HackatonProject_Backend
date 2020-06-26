from rest_framework import serializers
from .models import *


class FacultadSz(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'


class EscuelaSz(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = '__all__'


class TagSz(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSz(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CollaboratorSz(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'

    def create(self, data):
        """ Prevent duplicity """
        collaborator = Collaborator.objects.filter(user=data['user'])

        if len(collaborator) == 0:
            collaborator = [Collaborator.objects.create(**data)]

        # Finally
        return collaborator[0]


class TagXCollaboratorSz(serializers.ModelSerializer):
    class Meta:
        model = TagXCollaborator
        fields = '__all__'

    def create(self, data):
        # get_or_create usage to avoid TagXCollaborator duplicity
        tag = data['tag']
        collaborator = data['collaborator']
        instance, new = TagXCollaborator.objects.get_or_create(
            tag=tag,
            collaborator=collaborator,
        )
        return instance
