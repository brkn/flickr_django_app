from django.db import models
from django.utils import timezone


class RecentSearch(models.Model):
    keyword = models.CharField(max_length=95)
    date_entry = models.DateTimeField(default=timezone.now)
