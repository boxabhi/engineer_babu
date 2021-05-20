from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
    return render(request , 'index.html')


def check(request):
    search = request.GET.get('search')
    print(search)
    payload = []
    if search:
        data = Region.objects.filter(region_name__icontains = search)
        for d in data:
            payload.append(d.region_name)
        
    return JsonResponse(payload , safe=False)
        
    
    