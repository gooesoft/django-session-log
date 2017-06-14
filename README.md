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

Basic Installation that will provide you with admin view of all session logs:

1.  Include `django-session-log` in your `requirements.txt` file.
2.  Add `session_log` to `INSTALLED_APPS` and migrate db.


Optionally you can add view that lets your users see all of their active sessions
and log out them. 

1.  Add `session_activity.middleware.SessionActivityMiddleware` to
    `MIDDLEWARE_CLASSES` after the
    `django.contrib.sessions.middleware.SessionMiddleware` and
    `django.contrib.auth.middleware.AuthenticationMiddleware` middleware
    classes. This step is optional and only required if you intend user to be
    able to see all his active sessions and log out them
2.  Add url config for session list and sign-out views:

    > ``` {.sourceCode .python}
    > url(r'^sessions/', include('session_activity.urls')),
    > ```

    Then link to the main view using `{% url "session_activity_list" %}`
    template tag.

3.  Optionally copy & modify the `session_list.html` template to match
    your look and feel expectations.

## Dependencies
`django-session-log` depends on `django>=1.11.2`,
`django-appconf>=0.6` and `python-dateutil`.

## Demo


There’s also an instant demo example that can be run from the cloned
repository:

    ./manage.py migrate
    ./manage.py runserver
    

## License

django-session-log is released under the MIT license.

## Other Resources

-   Original GitHub repository -
    <https://github.com/nigma/django-session-activity>
-   Original PyPi Package site -
    <http://pypi.python.org/pypi/django-session-activity>
