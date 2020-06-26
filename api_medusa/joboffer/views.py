from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class JobOfferList(generics.ListCreateAPIView):
    """
    GET: List all JobOffer registers
    POST: Create a new JobOffer register
    """
    serializer_class = JobOfferSz
    queryset = JobOffer.objects.all()


class TagXJOList(generics.ListCreateAPIView):
    """
    GET: List all JobOffer's Tags
    POST: Add a new Tag to JobOffers
    """
    serializer_class = TagXJOSz
    queryset = TagXJO.objects.all()


class PostulationList(generics.ListCreateAPIView):
    """
    GET: List all Postulation registers
    POST: Create a new Postulation register
    """
    serializer_class = PostulationSz
    queryset = Postulation.objects.all()


class ChatList(generics.ListCreateAPIView):
    """
    GET: List all Chat registers
    POST: Create a new Chat register
    """
    serializer_class = ChatSz
    queryset = Chat.objects.all()


class MessageList(generics.ListCreateAPIView):
    """
    GET: List all Message registers
    POST: Create a new Message register
    """
    serializer_class = MessageSz
    queryset = Message.objects.all()


class JobMatchList(generics.ListCreateAPIView):
    """
    GET: List all accepted job registers
    POST: Add a new accepted job

    Desccripcion: This model stores all accepted jobs
    """
    serializer_class = JobMatchSz
    queryset = JobMatch.objects.all()


""" Custom views """


class SelectPostulant(APIView):
    """
    Descripcion:
        This view is used to select a postulation, and no more
    Params:
        postulation (pk)
    """

    def post(self, req):
        postulation_pk = req.data['postulation']
        try:
            postulation = Postulation.objects.get(pk=postulation_pk)
        except Postulation.DoesNotExist:
            # Postulation register with received pk does not exists
            return Response(
                data={"error_detail": "Postulation does not exists"},
                status=400
            )
        # Postulation exists
        postulations = Postulation.objects.filter(jo=postulation.jo, selected=True)
        if not len(postulations) < 3:
            return Response(
                data={"error_detail": "Postulation doesn't accept more than 3 selected"},
                status=400
            )
        # There are lesser than 3 selected postulations
        postulation.selected = True
        postulation.save()
        # Only return status=200, no data
        return Response(status=200)


class AcceptPostulant(APIView):
    """
    Descripcion:
        This view is used to accept a postulation, and no more
    Params:
        postulation (pk)
    """

    def post(self, req):
        postulation_pk = req.data['postulation']
        try:
            postulation = Postulation.objects.get(pk=postulation_pk)
        except Postulation.DoesNotExist:
            # Postulation register with received pk does not exists
            return Response(
                data={"error_detail": "Postulation does not exists"},
                status=400
            )
        # Postulation exists
        postulations = Postulation.objects.filter(jo=postulation.jo, accepted=True)
        if not len(postulations) == 0:
            return Response(
                data={"error_detail": "Postulation already have a postulation accepted"},
                status=400
            )
        # There is no accepted postulation
        postulation.accepted = True
        postulation.save()
        # Only return status=200, no data
        return Response(status=200)
