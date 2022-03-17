import uuid

from django.db import models
from django.utils import timezone

from accounts.models import User


class Diary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        related_name='diaries',
        on_delete=models.CASCADE
    )
    content = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    date = models.DateField()


class Flower(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dairies = models.ForeignKey(
        Diary, on_delete=models.SET_NULL, related_name="flower", null=True
    )
    name = models.CharField(max_length=20)
    sumbol = models.CharField(max_length=20)


class Photo(models.Model):
    def photo_upload_path(instance, filename):
        date_path = timezone.now().strftime("%Y/%m/%d")
        # name = os.path.splitext(filename)[-1].lower()
        return f"{date_path}/{filename}"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dairies = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(
        upload_to=photo_upload_path,
        null=True,
        blank=True,
    )
