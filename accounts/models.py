from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return "%s with %s year old" % (self.username, self.age)

    def get_absolute_url(self):
        return reverse('home_url', args=[self.pk, ])
