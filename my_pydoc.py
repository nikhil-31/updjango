import django
import pydoc
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'updjango.settings'
django.setup()
pydoc.cli()

# Added support for py docs
# python my_pydoc.py
