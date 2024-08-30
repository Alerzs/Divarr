from django.db import models


class Costumer(models.Model):
    name = models.CharField(max_length=15)

class Agahi(models.Model):
    title = models.CharField(max_length=25)
    text = models.TextField()
    writer = models.ForeignKey(Costumer)



