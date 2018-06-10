import uuid

from django.db import models


class Deployment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField(max_length=128, null=False, blank=False, editable=False)
    image = models.CharField(max_length=128, null=False, blank=False, editable=False)
    tag = models.CharField(max_length=128, null=False, blank=False, editable=False)
    timestamp = models.DateTimeField(null=False)

    def __repr__(self):
        return f'Deployment {self.full_image_name}'

    @property
    def full_image_name(self):
        return f'{self.host}/{self.image}:{self.tag}'
