from django.db import models


class Facultad(models.Model):
    code = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)


class Escuela(models.Model):
    code = models.CharField(primary_key=True, max_length=255)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=255)


class User(models.Model):
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)


class Collaborator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    settings = models.TextField()  # stringified JSON field


class TagXCollaborator(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
