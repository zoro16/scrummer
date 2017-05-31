from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import requests
import json
from django.conf import settings


class Consumer:
    TOKEN_URL = 'https://bitbucket.org/site/oauth2/access_token'
    AUTHORIZE_URL = 'https://bitbucket.org/site/oauth2/authorize'
    BASE_URL = 'https://api.bitbucket.org/'


def get_session():
    consumer = Consumer()
    client = BackendApplicationClient(
        client_id=settings.BITBUCKET_CONSUMER_KEY
    )
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(
        token_url=consumer.TOKEN_URL,
        client_id=settings.BITBUCKET_CONSUMER_KEY,
        client_secret=settings.BITBUCKET_CONSUMER_SECRET
    )
    token = dict(token)
    return token


def get_issue(issue_no):
    consumer = Consumer()
    url = '{}2.0/repositories/{}/{}/issues/{}'.format(consumer.BASE_URL,
                                                   settings.BITBUCKET_CONSUMER_USERNAME,
                                                   settings.BITBUCKET_REPO_SLUG,
                                                   issue_no)

    token = get_session()
    access_token = token['access_token']

    payload = {'access_token': access_token}
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.get(url, headers=headers, params=payload)
    response_str = response.content.decode("utf-8")
    response_json = json.loads(response_str)
    return response_json


# this will get the list of all the issues / will be used later on
def get_all_issues():
    consumer = Consumer()
    url = '{}2.0/repositories/{}/{}/issues'.format(consumer.BASE_URL,
                                                   settings.BITBUCKET_CONSUMER_USERNAME,
                                                   settings.BITBUCKET_REPO_SLUG)

    token = get_session()
    access_token = token['access_token']

    payload = {'access_token': access_token}
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.get(url, headers=headers, params=payload)
    response_str = response.content.decode("utf-8")
    response_json = json.loads(response_str)
    return response_json
