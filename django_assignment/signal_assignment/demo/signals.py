import time
import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TestModel, Auditlog

@receiver(post_save, sender = TestModel)
def signal_handler(sender, instance, **kwargs):

    print(" \n ======== Signal started =======")
    print("signal thread ID:",threading.get_ident())

    time.sleep(5)

    Auditlog.objects.create(
        message= "Created by signal"
    )
    print("====== Signal finished====== \n")