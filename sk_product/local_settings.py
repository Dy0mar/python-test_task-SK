"""
Django local settings for sk_product project.

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sk_db',
        'USER': 'sk_user',
        'PASSWORD': 'sk_pass',
        'HOST': '',
    }
}
