from django.http import JsonResponse
from django.shortcuts import render
from .models import Number
import json

def index(request):
    return render(request, 'MainView/index.html')

def add_number(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        number = Number(value=int(data['number']))
        number.save()
        return JsonResponse({'status': 'success'})

def show_content(request):
    numbers = Number.objects.all()
    number_list = [num.value for num in numbers]
    return JsonResponse({'numbers': number_list})

def calculate_sum(request):
    numbers = Number.objects.all()
    total_sum = sum(num.value for num in numbers)
    Number.objects.all().delete()
    return JsonResponse({'sum': total_sum})
