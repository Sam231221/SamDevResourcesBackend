from django.contrib import admin
from django.shortcuts import HttpResponse
from django.urls import path, include

def homeView(request):
    return HttpResponse("There is nothing here.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView ),
    path('api/', include('Mapp.urls')),
]
