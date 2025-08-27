
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("<h1>Hello, World! This is my first Django page.</h1>")