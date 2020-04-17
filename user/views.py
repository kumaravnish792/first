from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	employees = Employee.objects.all()
	# chart data
	data = [
         ['Year', 'Sales', 'Growth', 'Profit'],
         ['2014', 500, 400, 200],
         ['2015', 120, 460, 250],
      	['2016', 660, 120, 300],
         ['2017', 130, 540, 350]
      ]
 
	return render(request, 'user/main.html', {'employees':employees, 'data': data })
