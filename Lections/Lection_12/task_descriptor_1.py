from django.db import models


class Person(models.Models):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
