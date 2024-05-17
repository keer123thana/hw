from django.shortcuts import render
from app3.forms import inputform1
def home(request):
    if request.method=='POST':
        form1=inputform1(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            fname=data.get("input1")
            s1="congrats" + fname +'your account number is 4000'
            return render(request,'app3/index.html',{'param1':s1})
    else:
        form1=inputform1()
    return render(request,'app3/index.html',{'form':form1})
# Create your views here.
