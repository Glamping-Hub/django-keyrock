# django-keyrock

[![Code Climate](https://codeclimate.com/github/Glamping-Hub/django-keyrock/badges/gpa.svg)](https://codeclimate.com/github/Glamping-Hub/django-keyrock)

KeyRock Identity Manager client for Django

Made by [https://glampinghub.com](https://glampinghub.com)

## How to Install

1. Install it:
    ```sh
    pip install django-keyrock
    ```

2. Add 'keyrock' to your INSTALLED_APPS:
    ```python
    INSTALLED_APPS += ('keyrock',)
    ```
    
3. Add the context processor to your Django settings: 
    ```python
    TEMPLATE_CONTEXT_PROCESSORS += (
        'keyrock.context_processors.keyrock_url',
    )
    ```
    
4. Add KEYROCK_URL to your Django settings: 
    ```python
    KEYROCK_URL = 'your_domain'  # Example: KEYROCK_URL = 'https://yoursite.com' 
    ```
    
5. Add the urls to urls.py:
    ```python
    urlpatterns += patterns(
        '',
        url(r'keyrock/', include('keyrock.urls')),
    ) 
    ```
6. The url to sign up:
    ```html
        <a href="{{ KEYROCK_URL }}/sign_up/">
           Sign Up
        </a>
    ```
    
7. You can add a link to reset password:
    ```html
        <a href="{{ KEYROCK_URL }}/password/request/">
           Forgot your password/email?
        </a>
    ```
  
## Settings

**KEYROCK_APP_CLIENT_ID** Application ID in Keyrock. When you create your
application in Keyrock it will generate a pair of keys for it, this is the
generated id.

**KEYROCK_APP_CLIENT_SECRET** Application Secret in Keyrock. When you create
your application in Keyrock it will generate a pair of keys for it, this is the
generated secret.

**KEYROCK_REDIRECT_URL** URL to redirect to when the login/signup
process is completed. It must be a URL without parameters. Typically your
homepage URL.

**KEYROCK_URL** KeyRock instance URL, including protocol. Example:
*https://keyrock.example.com*

## Legal Notice

This software is licensed under a BSD 3-clause. You can find a copy of the
license in this repository.

Copyright (c) 2016, Glamping Hub <it@glampinghub.com>
