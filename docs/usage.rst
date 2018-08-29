=====
Usage
=====

To use Django DB Log in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_db_log.apps.DjangoDbLogConfig',
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
