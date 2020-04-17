from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	employees = Employee.objects.all()
 
	# chart data
   all_entries = Chart.objects.all()
   
   chart_data = [
         ['Year', 'Sales', 'Growth', 'Profit']
   ]
   
   for entries in all_entries:
      chart_data.append([
         entries.year,
         entries.sales,
         entries.growth,
         entries.profit
      ])
 
	return render(request, 'user/main.html', {'employees':employees, 'data': chart_data })
