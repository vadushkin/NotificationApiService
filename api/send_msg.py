import os
import requests
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from django.shortcuts import get_object_or_404
from .models import Client, Mailing, Message

logging.basicConfig(
    level=logging.DEBUG,
    filename=__file__ + '.log',
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s',
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('my_logger.log', maxBytes=50000000,
                              backupCount=5)
logger.addHandler(handler)

URL = 'https://probe.fbrq.cloud/v1/send/'
TOKEN = os.environ.get('API_TOKEN')
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def send_msg(msg_id, phone, text, ):
    """Отправка сообщения"""
    data = {
        'id': msg_id,
        'phone': phone,
        'text': text
    }
    try:
        response = requests.post(
            url=f'{URL}{msg_id}',
            headers=HEADERS,
            json=data
        )
        if msg_id.start_datetime > msg_id.finish_datetime:
            logger.debug(f'Отправка рассылки {msg_id.id}')
            send_msg(data)
            logger.debug(f'Отправка рассылки {msg_id.id} завершена')
    except requests.RequestException as e:
        logger.debug(f'Ошибка {e}')
    else:
        Message.objects.filter(pk=msg_id).update(status=response.status)


def process_distribution(data):
    """Проверка на время и отправка сообщения"""
    mailing = get_object_or_404(
        Mailing,
        id=data.get('id')
    )

    # проверка на время
    start_date = data.get('start_datetime')

    if not start_date or start_date > str(datetime.now()):
        return None

    finish_date = data.get('finish_datetime')

    if finish_date < str(datetime.now()):
        return None
    else:
        msg = Message.objects.create(mailing=mailing, client=Client)
        send_msg(msg.id, int(Client.phone_number), data.get('text'))
