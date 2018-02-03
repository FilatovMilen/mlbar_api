from django.db import models


class Recipe(models.Model):
    name = models.TextField()
    description = models.TextField()
