from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html', {'name':'JiaJie'})
    # return HttpResponse("<h1>hello world my name is jia jie</h1>")


def add(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2

    return render(request, 'results.html', {'result': res})