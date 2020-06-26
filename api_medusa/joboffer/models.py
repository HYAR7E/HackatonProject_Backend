from django.db import models
from master.models import User, Tag, Collaborator


class JobOffer(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


class TagXJO(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    jo = models.ForeignKey(JobOffer, on_delete=models.CASCADE)


class Postulation(models.Model):
    jo = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    message = models.TextField()
    selected = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    jo = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class JobMatch(models.Model):
    """ JobOffer accepted and theoretically done """
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
