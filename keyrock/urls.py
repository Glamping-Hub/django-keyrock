# Copyright (C) 2016 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'keyrock.views',

    url(r'oauth/authorize', 'keyrock_start_authorization', name='keyrock_start_authorization'),
    url(r'oauth/callback$', 'keyrock_oauth_callback', name='keyrock_oauth_callback'),
    url(r'oauth/data', 'keyrock_profile', name='keyrock_profile'),
)
