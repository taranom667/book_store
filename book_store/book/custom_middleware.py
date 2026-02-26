import time
from http.client import HTTPResponse


class CustomMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)
        duration = time.time() - start_time
        print(f"request time:{duration}")

        return response
