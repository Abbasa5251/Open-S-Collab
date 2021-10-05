from django.db import models
from rest_framework.serializers import SerializerMethodField
from .models import Project


class ProjectSerializer(SerializerMethodField):
    class Meta:
        model = Project
        fields = "__all__"
