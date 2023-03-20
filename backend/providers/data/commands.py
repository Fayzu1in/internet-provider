from django.core.management.base import BaseCommand
from bot import bot 

class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **options):
        # Call the start_bot() function from bot.py
        bot.infinity_polling()
