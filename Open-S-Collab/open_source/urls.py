from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.schemas import get_schema_view
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("project/", include("projects.urls")),
    path(
        "get-schema",
        get_schema_view(
            title="Your project", description="api for all things", version="1.0.0"
        ),
        name="open-schema",
    ),
    path("", include_docs_urls(title="Projects")),
    path("project/", include_docs_urls(title="Projects")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
