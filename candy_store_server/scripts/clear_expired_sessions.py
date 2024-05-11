#!/usr/bin/env python

import os

import django
from django.core.management import call_command


def clear_sessions():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "candy_store_server.settings")
    django.setup()
    call_command('clearsessions')


if __name__ == "__main__":
    clear_sessions()
