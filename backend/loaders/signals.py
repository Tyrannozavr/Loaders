from decimal import Decimal

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Incidents, Loader
from .services import update_loader_status, process_loader_status


@receiver(post_save, sender=Incidents, weak=False)
def request_round_complete(sender, instance, **kwargs):
    update_loader_status(incident_id=instance.pk)
    print('updated', instance)
    print(instance.__dict__)

@receiver(post_delete, sender=Incidents, weak=False)

def request_round_complete(sender, instance, **kwargs):
    process_loader_status(loader_id=instance.loader_id)
    # print('deleted', instance)
    # print(instance.__dict__)
    # update_loader_status(incident_id=instance.pk)



