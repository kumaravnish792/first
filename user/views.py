from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
	employees = Employee.objects.all()

	return render(request, 'user/main.html', {'employees':employees})
