# django-keyrock

KeyRock Identity Manager client for Django

Made by [https://glampinghub.com](https://glampinghub.com)

## How to Install

Clone the repository and then follow this:
[https://docs.python.org/2/install/](https://docs.python.org/2/install/)

## Settings

**KEYROCK_APP_CLIENT_ID** Application ID in Keyrock. When you create your
application in Keyrock it will generate a pair of keys for it, this is the
generated id.

**KEYROCK_APP_CLIENT_SECRET** Application Secret in Keyrock. When you create
your application in Keyrock it will generate a pair of keys for it, this is the
generated secret.

**KEYROCK_COMPLETED_LOGIN_URL** URL to redirect to when the login/signup
process is completed. It must be a URL without parameters. Typically your
homepage URL.

**KEYROCK_URL** KeyRock instance URL, including protocol. Example:
*https://keyrock.example.com*

**KEYROCK_YOUR_SERVER_PROTOCOL** If your Site includes the domain (it starts
with *http*) then you can ignore this setting. Else you need to specify the
protocol of your application here. Possible values are *http://* and *https://*

## Legal Notice

This software is licensed under a BSD 3-clause. You can find a copy of the
license in this repository.

Copyright (c) 2016, Glamping Hub <it@glampinghub.com>
