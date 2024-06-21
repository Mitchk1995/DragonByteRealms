# user_auth/middleware.py

from django.utils.deprecation import MiddlewareMixin

class TokenAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'Authorization' in request.headers:
            auth = request.headers.get('Authorization').split()
            if len(auth) == 2 and auth[0].lower() == 'bearer':
                request.META['HTTP_AUTHORIZATION'] = request.headers['Authorization']
