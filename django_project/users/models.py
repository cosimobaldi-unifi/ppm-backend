from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    ATTENDEE = "attendee"
    ORGANIZER = "organizer"

    ROLE_CHOICES = [
        (ATTENDEE, "Attendee"),
        (ORGANIZER, "Organizer"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ATTENDEE,
    )

    def is_organizer(self):
        return self.role == self.ORGANIZER