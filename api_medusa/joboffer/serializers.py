from rest_framework import serializers
from .models import *


class JobOfferSz(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = '__all__'


class TagXJOSz(serializers.ModelSerializer):
    class Meta:
        model = TagXJO
        fields = '__all__'

    def create(self, data):
        # get_or_create usage to avoid TagXJO duplicity
        tag = data['tag']
        jo = data['jo']
        instance, new = TagXJO.objects.get_or_create(
            tag=tag,
            jo=jo,
        )
        return instance


class PostulationSz(serializers.ModelSerializer):
    class Meta:
        model = Postulation
        fields = '__all__'


class ChatSz(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class MessageSz(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class JobMatchSz(serializers.ModelSerializer):
    class Meta:
        model = JobMatch
        fields = '__all__'
