import logging
from django.db import transaction, OperationalError
from nl.celery import app
from celery.utils.log import get_task_logger
from core.models import ContentBase

logger = get_task_logger(__name__)
logging.basicConfig(filename='celery.txt', level=logging.DEBUG)


@app.task
def update_hits_task(contentbase_id):
    """Increases the counter for content"""
    # Must be in a transaction to grab a lock
    with transaction.atomic():
        try:
            content = ContentBase.objects.select_for_update(nowait=True).get(id=contentbase_id)
        except OperationalError:
            raise ContentBase.HitInProgress

        return content._hit()

