# everest_broker/middleware.py
from django.utils.deprecation import MiddlewareMixin
import json

class LogPostMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST':
            try:
                data = json.loads(request.body.decode('utf-8'))
                print(f"Received POST request on {request.path}: {data}")
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
        return None
