from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().lower()
        if host == 'cris96spa.com':
            return HttpResponsePermanentRedirect(f"https://www.{host}{request.path}")
        return self.get_response(request)