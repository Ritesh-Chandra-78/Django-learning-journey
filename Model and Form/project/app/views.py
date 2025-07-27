from django.shortcuts import render,redirect
from .forms import Myform,ContactForm
from django.contrib import messages


# Create your views here.
def Form(request):
    fm = Myform()
    return render(request,'form.html',{'fm':fm})


def ModelForm(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Form submitted successfully')
            return redirect('login')
        else:
            messages.error(request,'Form Submission failed')
    else:
        fm = ContactForm()
    return render(request,'modelform.html',{'fm':fm})



def login(request):
    return render(request,'login.html')