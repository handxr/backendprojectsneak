from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(
        'categories.Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
