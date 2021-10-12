from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


class ViewProjects(generics.ListAPIView):
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer


class CreateProject(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serilizer = ProjectSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save(owner=request.user.profile)
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
