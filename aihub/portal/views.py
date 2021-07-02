from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Model
from .models import Student
# Create your views here.

def home(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def admins (request):
    students = Student.objects.all()
    return render(request, 'show.html', {'student':students})

def search_result (request):
    if request.method == "POST":
        searched_result = request.POST['searched_result']
        modelresult = Model.objects.filter(modelName__contains=searched_result),
        return render(request, 'search_result.html',
        {'searched_result' : searched_result,
        'models': modelresult})

def model_view (request):
    models = Model.objects.all()
    return render (request, 'search_result.html', models)

def show (request):
    return render(request,"show.html")
# @csrf_exempt
# def add(request):

#     val1 = request.POST['username']
#     val2 = request.POST['password']
#     status = 'successful'

#     return render(request, 'results.html', {'user' : val1, 'pass' : val2,'result': status})