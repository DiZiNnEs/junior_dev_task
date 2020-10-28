from django.db import models


class University(models.Model):
    university_name = models.CharField(max_length=32)
    university_description = models.CharField(max_length=200)
