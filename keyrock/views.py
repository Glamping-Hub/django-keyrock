# Copyright (C) 2016 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

import base64

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.site.models import Site

from requests_oauthlib import OAuth2Session
import requests


authorization_base_url = '{}/oauth2/authorize'.format(settings.KEYROCK_URL)
token_url = '{}/oauth2/token'.format(settings.KEYROCK_URL)


def get_redirect_uri():
    site = Site.objects.get_current()
    protocol = ''
    if not site.domain.startswith('http'):
        protocol = settings.KEYROCK_YOUR_SERVER_PROTOCOL
    return '{}{}/keyrock/oauth/callback'.format(protocol, site.domain)


def keyrock_start_authorization(request):
    keyrock = OAuth2Session(settings.KEYROCK_APP_CLIENT_ID)
    authorization_url, state = keyrock.authorization_url(authorization_base_url)
    authorization_url += '&redirect_uri={}'.format(get_redirect_uri())
    return HttpResponseRedirect(authorization_url)


def keyrock_oauth_callback(request):
    state = request.build_absolute_uri().split('state=')[1].split('&')[0]
    keyrock = OAuth2Session(settings.KEYROCK_APP_CLIENT_ID, redirect_uri=get_redirect_uri(), state=state)
    basic_auth = base64.b64encode('{}:{}'.format(settings.KEYROCK_APP_CLIENT_ID, settings.KEYROCK_APP_CLIENT_SECRET))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic {}'.format(basic_auth)
    }
    token = keyrock.fetch_token(token_url, client_secret=settings.KEYROCK_APP_CLIENT_SECRET,
                                code=request.build_absolute_uri().split('code=')[1].split()[0],
                                verify=False,
                                headers=headers)
    request.session['oauth_token'] = token
    return HttpResponseRedirect(reverse('keyrock_profile'))


def keyrock_profile(request):
    access_token = request.session['oauth_token']['access_token']
    url = '{}/user'.format(settings.KEYROCK_URL)
    params = {
        'access_token': access_token
    }
    r = requests.get(url, params=params, verify=False)
    json_data = r.json()
    username = json_data['email']
    email = json_data['email']
    display_name = json_data['displayName'].split(' ')
    first_name = display_name[0]
    last_name = ' '.join(display_name[1:])

    user_model = get_user_model()

    try:
        user = user_model.objects.get(email__iexact=email)
    except user_model.DoesNotExist:
        user = user_model()

    user.username = username
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    login(request, user)

    redirect_to = settings.KEYROCK_COMPLETED_LOGIN_URL
    return HttpResponseRedirect(reverse(redirect_to))
