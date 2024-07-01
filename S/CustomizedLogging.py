#filters.py
import logging

class UsernameFilter(logging.Filter):
    def filter(self, record):
        try:
            from django.utils.thread_support import get_current_request
            request = get_current_request()
            record.username = request.user.username
        except Exception:
            record.username = 'Anonymous'
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
        'standard': {
            'format': '[{asctime}] {username} "{message}"',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'useRecords.log'),
            'formatter': 'standard',
            'filters': ['username_filter'],
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': ['username_filter'],
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': False,
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


import threading

_thread_locals = threading.local()

def get_current_request():
    return getattr(_thread_locals, 'request', None)

class ThreadLocalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.request = request
        response = self.get_response(request)
        return response

