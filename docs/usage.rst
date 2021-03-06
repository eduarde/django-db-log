=====
Usage
=====

To use Django DB Log in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_apscheduler',
        'django_db_log',
        ...
    )

Add Django DB Log's URL patterns:

.. code-block:: python

    from django_db_log import urls as django_db_log_urls


    urlpatterns = [
        ...
        url(r'^', include(django_db_log_urls)),
        ...
    ]

Add the LOGGING configuration in the settings.py file.

.. code-block:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
               'format': '[%(asctime)s] %(levelname)s %(module)s.%(funcName)s %(lineno)d: %(message)s'
            },
            'simple': {
                'format': ' %(levelname)s  %(message)s',
            },
        },
        'handlers': {
            'log_db': {
                'level': 'ERROR',
                'class': 'django_db_log.handlers.DBHandler',
                'model': 'django_db_log.models.ErrorLog',
                'expiry': 86400,
                'formatter': 'simple',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['log_db'],
                'level': 'ERROR',
                'propagate': False,
            },
        },
    }

Add the following constants in your settings file. These will be used to determine the lookup days to delete old logs from db.

.. code-block:: python

    INTERVAL_SCHEDULER_JOB_SECONDS = 43200
    GENERAL_LOGS_DELETE_DAYS = 2
    INFO_LOGS_DELETE_DAYS = 2
    DEBUG_LOGS_DELETE_DAYS = 2
    ERROR_LOGS_DELETE_DAYS = 10

Run migrations

.. code-block:: python

    python manage.py migrate
