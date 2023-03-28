from django.db.models.signals import post_save
from django.dispatch import receiver
from telegram import Bot

import os
import django
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()
from data.models import Callback

TOKEN = '6234504758:AAEF-Fa6S6VSxYAO8kYR5aiD9K8dRYq5Nq8'

@receiver(post_save, sender=Callback)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:
        bot = Bot(token=TOKEN)
        chat_id = 657061394
        message = f'A new instance of MyModel was added: {instance}'
        bot.send_message(chat_id=chat_id, text=message)


