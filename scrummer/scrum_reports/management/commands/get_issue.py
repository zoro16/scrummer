from django.core.management.base import BaseCommand
import bitbucket_oauth2


class Command(BaseCommand):

    help = "Get Bitbucket Issues by passing the issue's number"
    
    def add_arguments(self, parser):
        parser.add_argument('issue_no', type=str)

    def handle(self, *args, **options):
        issue = bitbucket_oauth2.get_issue(issue_no=options['issue_no'])
        issue_id = str(issue['id'])
        issue_title = issue['title']
        issue_content = issue['content']['raw']
        print('{"id":"' + issue_id + '","title":"' + issue_title +
              '","content":"' + issue_content + '"}'
        )
