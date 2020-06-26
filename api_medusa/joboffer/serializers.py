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

    def validate(self, data):
        print(data)
        print(data['jo'].client)
        print(data['collaborator'].user)
        if data['jo'].client == data['collaborator'].user:
            raise serializers.ValidationError("Client can't apply to his own JobOffer")
        return data

    def create(self, data):
        """ Prevent duplicity """
        postulation = Postulation.objects.filter(collaborator=data['collaborator'])

        if len(postulation) == 0:
            postulation = [Postulation.objects.create(**data)]

        # Finally
        return postulation[0]


class MessageSz(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ChatSz(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = [
            'jo', 'client', 'collaborator', 'created',
            'messages'  # Custom
        ]

    def get_messages(self, instance):
        """ Get this chat messages """
        return MessageSz(
            Message.objects.filter(chat=instance),
            many=True
        ).data


class JobMatchSz(serializers.ModelSerializer):
    class Meta:
        model = JobMatch
        fields = '__all__'
