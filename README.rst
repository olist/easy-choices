easy-choices
=============

.. image:: https://circleci.com/gh/olist/easy-choices.svg?style=shield
    :target: https://circleci.com/gh/olist/easy-choices


It's a library deeply inspired by Choices from `django-model-utils`_.
However, sometimes we just need to use Choices rather than all the features provided by `django-model-utils`_.

.. _django-model-utils: https://django-model-utils.readthedocs.io/


Requirements
------------

* Python >= 3.5


Usage
-----

The ``easy-choices`` package is hosted on our `PyPI repository`_.

.. _PyPI repository: https://pypi.org/user/olist/

You can install the latest version of ``easy-choices`` using pip:

.. code-block:: bash

   $ pip install easy-choices


And use easy-choices as it's demonstrated below:


.. code-block:: python

    from django.db import models
    from easy_choices import Choices

    status_choices = Choices(
        ("sent", "Sent"),
        ("delivered", "Delivered"),
    )

    class Product(models.Model)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        status = models.CharField(max_length=10, choices=status_choices.to_django_choices())

        @property
        def is_delivered(self):
            # You can use status_choices as a Enum
            return self.status == status_choices.delivered
