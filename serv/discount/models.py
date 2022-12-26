from django.db import models


class SupplierDiscount(models.Model):
    discount = models.FloatField()
    discounted_record = models.OneToOneField(
        'supplier.CarPriceRelationSupplier',
        models.CASCADE,
        related_name='discount'
    )
    is_active = models.BooleanField(default=True)

    def safe_delete(self):
        self.is_active = False
        self.save()


class CarShowroomDiscount(models.Model):
    discount = models.FloatField()
    discounted_record = models.OneToOneField(
        'carshowroom.CarPriceRelationShowroom',
        models.CASCADE,
        related_name='discount'
    )
    is_active = models.BooleanField(default=True)

    def safe_delete(self):
        self.is_active = False
        self.save()
