#filters.py
import logging

class UsernameFilter(logging.Filter):
    def filter(self, record):
        from django.contrib.auth.models import AnonymousUser
        from threading import current_thread

        request = getattr(current_thread(), 'request', None)
        if request:
            user = getattr(request, 'user', AnonymousUser())
            record.username = user.username if user.is_authenticated else 'AnonymousUser'
        else:
            record.username = 'N/A'
        return True


#settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'username_filter': {
            '()': 'path.to.filters.UsernameFilter',
        },
    },
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message} user={username}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message} user={username}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['username_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'filters': ['username_filter'],
            'class': 'logging.FileHandler',
            'filename': 'django.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

MIDDLEWARE = [
    # ... 其他中间件 ...
    'path.to.middleware.RequestMiddleware',
]



#middleware.py
from threading import current_thread

class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_thread().request = request
        response = self.get_response(request)
        return response
