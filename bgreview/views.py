from django.http import HttpResponse


def get(request):
    return HttpResponse("<pre>Hello world</pre>")
