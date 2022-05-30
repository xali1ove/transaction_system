from .celery import app
from .models import Client
from django.db.utils import OperationalError
from django.db import transaction
import logging


logger = logging.getLogger(__name__)


@app.task
def change_balance(client: Client, value: float):
    try:
        with transaction.atomic():
            client.balance_value += float(value)
            if client.balance_value >= 0 and float(value) != 0:
                client.save()
    except OperationalError as exc:
        logger.error(str(exc))
        change_balance.apply_async([client, value], countdown=5)
