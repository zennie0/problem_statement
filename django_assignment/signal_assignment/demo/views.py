import threading

from django.http import HttpResponse
from django.db import transaction

from .models import TestModel


#after save will appear only after signal completes 
#that means signals are synchronous by default
def test_sync(request):
    print("\nBefore Save")

    TestModel.objects.create(
        name="Sync Test"
    )

    print("After save \n")

    return HttpResponse("sync test complete")

#caller thread and signal thread will be same
#that means signals run in the same thread
def test_thread(request):
    print(
        "\n caller thread Id:",
        threading.get_ident()
    )

    TestModel.objects.create(
        name="Thread Test"
    )

    return HttpResponse("thread test completed")

#signals run in the same database transaction as caller
def test_transaction(request):
    try:
        with transaction.actomic():
            TestModel.objects.create(
                name="Tramsaction Test"
            )

            raise Exception(
                "Rollback Transaction"
            )
        
    except Exception:
        pass

    return HttpResponse(
        "transaction test completed"
    )


