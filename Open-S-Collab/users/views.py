# import for authentication
from rest_framework import status
from django.contrib.auth.models import User

# import for forms and models
from .models import Profile

# imports for api
from .serializers import *
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

model = Profile.objects.all()
auth = User.objects.all()

# custom class for permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


# view for getting all the profile
class Profiles(generics.ListAPIView):
    queryset = model
    serializer_class = ProfileSerializer


# view for getting a profile in detailed view
class SingleProfile(generics.RetrieveAPIView):
    queryset = model
    serializer_class = ProfileSerializer


# view for updating the profile if the the PUT request is done by the owner
class updateProfile(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user.profile


# view for registering a user
class Registering(APIView):
    def post(self, request):
        reg_serializer = UserSerializer(data = request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return  Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)