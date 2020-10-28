from django.db import models


class University(models.Model):
    university_name = models.CharField(max_length=32)
    address = models.CharField(max_length=50)
    university_description = models.CharField(max_length=200)
    items = models.CharField(max_length=100, default='Not filled by authors')

    def __str__(self):
        return self.university_name + ' ' + self.university_description
