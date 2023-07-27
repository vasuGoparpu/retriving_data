from django.shortcuts import render

# Create your views here.



def data(request):
    d={'name':'NANDA','age':16}
    return render(request,'data.html',context=d)