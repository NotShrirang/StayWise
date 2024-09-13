from django.db import models
import uuid

from places.models import Place

class PlaceReservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reservations')
    user = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.place} (from {self.start_datetime} to {self.end_datetime})"
