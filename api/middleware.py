import json
import time
from threading import local

thread_locals = local()


class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        thread_locals.path = request.path
        thread_locals.sql_count = 0
        thread_locals.sql_total = 0
        timestamp = time.monotonic()

        response = self.get_response(request)

        data = {
            'path': request.path,
            'request_total': round(time.monotonic() - timestamp, 3),
            'sql_count': round(thread_locals.sql_count, 3),
            'sql_total': round(thread_locals.sql_total, 3),
        }

        with open('request.log', 'a') as f:
            f.write(json.dumps(data) + '\n')

        thread_locals.sql_total = 0
        thread_locals.sql_count = 0
        thread_locals.path = ''

        return response
