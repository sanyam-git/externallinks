from .base import *

DEBUG = False

ALLOWED_HOSTS += ['wikilink-staging.wmflabs.org']

CRON_CLASSES += [
    'extlinks.links.cron.TotalLinksCron'
]

# Redirect HTTP to HTTPS
# SECURE_PROXY_SSL_HEADER is required because we're behind a proxy
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
