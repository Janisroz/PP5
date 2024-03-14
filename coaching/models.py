from django.db import models
from products.models import Product

# Create your models here.
class Coach(models.Model):
    """
    Model for Coaches
    """
    name = models.CharField(max_length=254)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    """
    Model for Sessions
    """
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL,
                              related_name="sessions", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                 related_name="sessions")
    title = models.CharField(max_length=254)
    description = models.TextField()
    exercises = models.TextField()