from django.http import HttpResponse

def index(request):
    return HttpResponse("Esta sera una pagina basica del blog.")


# Create your views here.
