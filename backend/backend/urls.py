from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a la API</h1><p>Visita <a href='/api/'>/api/</a> para explorar la API.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', home),  # Página raíz
]


