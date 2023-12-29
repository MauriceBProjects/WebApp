from django.db import models

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=100)
    order_from_sun = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/Sun.png')
    radius = models.IntegerField()

    def __str__(self):
        return self.name
