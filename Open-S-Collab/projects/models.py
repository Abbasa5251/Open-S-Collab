from django.db import models
from users.models import Profile


def upload_to(instance, filename):
    return f"projects/{filename}"


class Project(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=5000)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self):
        return str(self.title)
