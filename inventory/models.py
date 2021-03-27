from django.db import models

# Create your models here.

class Stock(models.Model):

    type = models.CharField(max_length=200, blank=False) #name of column
    quantity = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be distributed'),
        ('SOLD', 'Item already distributed'),
        ('NEEDS RESTOCKING', 'Item needs restocking')
    )

    status = models.CharField(max_length=50, choices=choices, default='SOLD')
    description = models.CharField(max_length=50, default=" ")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Quantity: {1}'.format(self.type, self.quantity)

class Kitchenware(Stock):
    pass

class Chicken(Stock):
    pass