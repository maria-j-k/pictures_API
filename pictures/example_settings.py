SECRET_KEY = '<your_secret_key>'

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database_name>',
        'HOST': '<host>',
        'PASSWORD': '<database user\'s password>',
        'USER': '<database_user_name>',
        'PORT': '<database_port_number>',
        }
   }
