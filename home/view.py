from django.http import HttpResponse
from django.template  import Context, loader

import requests


def home(request):
    context=Context({"name":"terry"})
    template = loader.get_template("home.html")
    return HttpResponse(template.render(context))
    