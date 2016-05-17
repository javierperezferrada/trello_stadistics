from django.core.management.base import BaseCommand, CommandError
from trello import TrelloApi

class Command(BaseCommand):
    help = 'collects information from api Trello'

    def handle(self, *args, **options):
        print 'hola mundo'
        TRELLO_APP_KEY = '8924e92319a65ea776ab9662041f57d8'
        trello = TrelloApi(TRELLO_APP_KEY)
        print trello.boards.get('4d5ea62fd76aa1136000000c')
