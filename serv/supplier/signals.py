from django.db.models import signals
from django.dispatch import receiver

from discount.models import SupplierDiscount
from supplier.models import CarPriceRelationSupplier


@receiver(signals.post_save, sender=SupplierDiscount)
def apply_discount(sender, instance, **kwargs):
    car_price = CarPriceRelationSupplier.objects.get(pk=instance.discounted_record.id)
    car_price.price_with_discount = car_price.price - car_price.price * (instance.discount / 100)
    car_price.save()


@receiver(signals.post_delete, sender=SupplierDiscount)
def disable_discount(sender, instance, **kwargs):
    car_price = CarPriceRelationSupplier.objects.get(pk=instance.discounted_record.id)
    car_price.price_with_discount = None
    car_price.save()


@receiver(signals.post_save, sender=CarPriceRelationSupplier)
def apply_price(sender, instance, created, **kwargs):
    if created:
        instance.price_with_discount = instance.price
        instance.save()
