from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
    # return HttpResponse("This is from show view functions.")
    # return HttpResponse("<h1>This is from show view functions.</h1>")
    data = {
        'name':'Rahul',
        'age':23,
        'gender':'male'
    }
    return render(request, "index.html", {'data': data}) 


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def more(request):
    return render(request,"more.html")
def contact(request):
    return render(request,"contact.html")