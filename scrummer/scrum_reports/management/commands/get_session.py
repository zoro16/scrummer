from django.core.management.base import BaseCommand
import bitbucket_oauth2


class Command(BaseCommand):

    help = "Get Bitbucket Access Token"

    def handle(self, *args, **options):
        token = bitbucket_oauth2.get_session()
        print(token)

