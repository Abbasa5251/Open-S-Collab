from django.db import models
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Project
from users.serializers import ProfileSerializer


class ProjectSerializer(ModelSerializer):
    owner = ProfileSerializer()
    image = serializers.ImageField()

    class Meta:
        model = Project
        fields = "__all__"
