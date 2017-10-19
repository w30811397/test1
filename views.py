from django.http import HttpResponse

def index(request):
    return HttpResponse('say hallo')

def index2(request):
    return HttpResponse('say bye')
