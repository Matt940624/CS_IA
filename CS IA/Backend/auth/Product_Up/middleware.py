from django import http
from django.core.handlers.wsgi import WSGIRequest


def log_middleware(get_response):
    def _middleware(request: WSGIRequest):
        print("\n\nRequest: \n")
        print(request.headers)
        response = get_response(request)

        print("\nResponse: \n")
        print(response, "\n\n")

        return response
    return _middleware


class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (request.method == "OPTIONS" and "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META):
            response = http.HttpResponse()
            response["Content-Length"] = "0"
            response["Access-Control-Max-Age"] = 86400
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "DELETE, GET, OPTIONS, PATCH, POST, PUT"
        response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Origin, Access-Control-Allow-Headers, Access-Control-Request-Method, Access-Control-Request-Headers, accept, accept-encoding, authorization, content-type, dnt, origin, user-agent, x-csrftoken, x-requested-with, referer"
        return response
