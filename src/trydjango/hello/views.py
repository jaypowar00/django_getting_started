from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    '''
    Gives http response 'Hello World'
    '''
    wow=False
    if 'wow' in request.GET:
        wow = request.GET['wow']
    if wow:
        return render(request,'index.html',{'name':'RedRanger','wow':wow})
    return render(request,'index.html',{'name':'RedRanger'})

def add(request):
    '''
    This function adds values
    '''
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    ans = n1 + n2

    return render(request,'result.html',{'result':ans})