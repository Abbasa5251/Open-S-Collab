from django.urls import path, include
from . import views

# importing the default router function for creating the register route
from rest_framework.routers import DefaultRouter

# import jwt token authentication view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


token = TokenObtainPairView.as_view()
token_refresh = TokenRefreshView.as_view()
authentication = [
    # Authentication
    path("auth/login/", token, name="token_obtain_pair"),
    path("auth/refresh/", token_refresh, name="token_refresh"),
    path("auth/register/", views.Registering.as_view()),
]


profile_detail = views.SingleProfile.as_view()
profile_list = views.Profiles.as_view()

profiles = [
    path("profiles", profile_list, name="profile_list"),
    path("profiles/<str:pk>/", profile_detail, name="profile_detail"),
    path("profiles/<str:pk>/update/", views.updateProfile.as_view()),
    path("edit-account", views.updateProfile.as_view()),
]
urlpatterns = []
urlpatterns += authentication
urlpatterns += profiles
