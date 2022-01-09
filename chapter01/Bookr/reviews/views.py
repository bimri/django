from django.http import HttpResponse, request


def index(request):
    name = request.GET.get("name") or "world" 
    return HttpResponse("Hello, {}!".format(name))
