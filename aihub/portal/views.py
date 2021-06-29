from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, 'login.html', {'name':'JiaJie'})
    # return HttpResponse("<h1>hello world my name is jia jie</h1>")

@csrf_exempt
def add(request):

    val1 = request.POST['username']
    val2 = request.POST['password']
    status = 'successful'

    return render(request, 'results.html', {'user' : val1, 'pass' : val2,'result': status})