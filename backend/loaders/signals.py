from decimal import Decimal

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Incidents, Loader
from .services import update_loader_status


@receiver(pre_save, sender=Incidents, weak=False)
def request_round_complete(sender, instance, **kwargs):
    update_loader_status(incident_id=instance.pk)
