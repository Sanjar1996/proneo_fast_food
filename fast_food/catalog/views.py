from django.http import JsonResponse
from django.shortcuts import render
from .models import Product_image, Category

def catalog(request):
    context={

    }
    return render(request, 'index.html',context)

def api_category(request):
    models = Category.objects.all()
    result = []
    for data in models:
        result.append({'name': data.name})

    return JsonResponse(result, safe=False)
