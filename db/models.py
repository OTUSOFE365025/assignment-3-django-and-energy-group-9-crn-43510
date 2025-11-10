from django.db import models


class Product(models.Model):
    """
    Represents a product in the cash register system.
    """
    upc = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=200)
    # store in cents to avoid float rounding errors
    price_cents = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.upc})"

    @property
    def price(self) -> float:
        """
        Return the price in dollars for display.
        """
        return self.price_cents / 100.0
