DEBUG = True

TEMPLATE_DEBUG = True

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
 	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'simplemooc',
        'USER': 'simple',
        'PASSWORD': 'simple123',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}