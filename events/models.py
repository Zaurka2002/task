from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.name