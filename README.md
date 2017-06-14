# django-session-log


Logs all sessions and sign-outs. Originally developed at [en.ig.ma
software shop].

Overview
========

- logging all sessions permanently
- logging off remote sessions
- logging of IP addresses and browser info


Quickstart
==========

1.  Include `django-session-activity` in your `requirements.txt` file.
2.  Add `session_activity` to `INSTALLED_APPS` and migrate/syncdb.
3.  Add `session_activity.middleware.SessionActivityMiddleware` to
    `MIDDLEWARE_CLASSES` after the
    `django.contrib.sessions.middleware.SessionMiddleware` and
    `django.contrib.auth.middleware.AuthenticationMiddleware` middleware
    classes.
4.  Add url config for session list and sign-out views:

    > ``` {.sourceCode .python}
    > url(r'^sessions/', include('session_activity.urls')),
    > ```

    Then link to the main view using `{% url "session_activity_list" %}`
    template tag.

5.  Optionally copy & modify the `session_list.html` template to match
    your look and feel expectations.

Dependencies
============

`django-session-activity` depends on `django>=1.5.0`,
`django-appconf>=0.6` and `python-dateutil`.

Documentation
=============

There’s also an instant demo example that can be run from the cloned
repository:

    ./manage.py migrate
    ./manage.py runserver
    

License
=======

django-session-log is released under the MIT license.

Other Resources
===============

-   GitHub repository -
    <https://github.com/nigma/django-session-activity>
-   PyPi Package site -
    <http://pypi.python.org/pypi/django-session-activity>
