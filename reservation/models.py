from django.db import models
import uuid

from places.models import Place
from users.models import StayWiseUser

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reservationsUsers')
    user = models.ForeignKey(StayWiseUser, on_delete=models.CASCADE, related_name='reservationsPlaces')
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        db_table = "staywise_reservations"
        managed = True

    def __str__(self):
        return f"{self.user} - {self.place} (from {self.start_datetime} to {self.end_datetime})"


class Ratings(models.Model):
    id = models.UUIDField(verbose_name="id", primary_key=True, default=uuid.uuid4, editable=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reservationRatings")
    user = models.ForeignKey(StayWiseUser, on_delete=models.CASCADE, related_name="userRatings")
    remarks = models.TextField(blank=True)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
        db_table = "staywise_ratings"
        managed = True
