[![Stories in Ready](https://badge.waffle.io/kvas-it/open360.png?label=ready&title=Ready)](https://waffle.io/kvas-it/open360)
# Open360 - simple 360-degree review app

Open360 is a very basic [360-degree review] [1] application built using Django.

Makefile can be used for performing basic tasks:

* Create virtualenv and install requirements:

        $ make env

* Create database:

        $ make db

* Run debug server:

        $ make run

At the moment most of the content can only be created using Django admin
interface. The only things that we have 'proper' UI for are creating the review
and filling out the review form (answer sheet). The way to get to it is more or
less as follows:

* [Create superuser] [2].
* Log into admin interface and create another user or two.
* Create a review template and some reviewer classes for it (they could be
  something like "self" and "colleague").
* Create some question groups and questions for the review template.
* Create some reviews and answer sheets using existing users as owners.
* Now the reviews can be filled out using the app UI.

[1]: https://en.wikipedia.org/wiki/360-degree_feedback
[2]: https://docs.djangoproject.com/en/1.8/ref/django-admin/#createsuperuser
