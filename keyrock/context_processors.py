# Copyright (C) 2016 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

from django.conf import settings


def keyrock_url(request):
    return {'keyrock_url': settings.KEYROCK_URL}
