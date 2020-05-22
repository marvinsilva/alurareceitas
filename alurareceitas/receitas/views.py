from django.http import HttpResponse


def index(request):
    return HttpResponse('<html><body><h1>Receitas</h1></body></html>', content_type='text/html')
