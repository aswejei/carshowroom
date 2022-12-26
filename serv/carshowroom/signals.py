from django.db.models import signals
from django.dispatch import receiver

from serv.discount.models import CarShowroomDiscount
from serv.carshowroom.models import CarPriceRelationShowroom


@receiver(signals.post_save, sender=CarShowroomDiscount)
def apply_discount(sender, instance, **kwargs):
    car_price = CarPriceRelationShowroom.objects.get(pk=instance.discounted_record)
    car_price.price_with_discount = car_price.price * (instance.discount / 100)
    car_price.save()


@receiver(signals.post_delete, sender=CarShowroomDiscount)
def disable_discount(sender, instance, **kwargs):
    car_price = CarPriceRelationShowroom.objects.get(pk=instance.discounted_record)
    car_price.price_with_discount = None
    car_price.save()


@receiver(signals.post_save, sender=CarPriceRelationShowroom)
def apply_price(sender, instance, created, **kwargs):
    if created:
        instance.price_with_discount = instance.price
        instance.save()
