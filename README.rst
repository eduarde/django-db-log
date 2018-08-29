=============================
Django DB Log
=============================

.. image:: https://badge.fury.io/py/django_db_log.svg
    :target: https://badge.fury.io/py/django_db_log

.. image:: https://travis-ci.org/eduarde/django_db_log.svg?branch=master
    :target: https://travis-ci.org/eduarde/django_db_log

.. image:: https://codecov.io/gh/eduarde/django_db_log/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/eduarde/django_db_log

Custom DB Log Handler for Django Projects.

Documentation
-------------

The full documentation is at https://django_db_log.readthedocs.io.

Quickstart
----------

Install Django DB Log::

    pip install django_db_log

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
