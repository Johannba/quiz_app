from django.db import models

class CarouselImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='carousel/')
