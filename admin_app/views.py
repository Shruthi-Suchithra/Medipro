from django.shortcuts import render,redirect
from user_app.models import usersinfo
from user_app.models import doctorsinfo
from user_app.models import appointmentsinfo

# Create your views here.


def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
def userview(request):
    data=usersinfo.objects.all()
    return render(request,'userview.html',{'users':data})

def userdelete(request,id):
    data=usersinfo.objects.get(pk=id)
    # primary key pk (it must be unique)
    
    data.delete()
    return redirect(userview)
def doctorview(request):
    data=doctorsinfo.objects.all()
    return render(request,'doctorview.html',{'doctordata':data})

def doctordelete(request,id):
    data=doctorsinfo.objects.get(pk=id)

    data.delete()
    return redirect(doctorview)
def adminapp_view(request):
    data=appointmentsinfo.objects.all()
    return render(request,'adminapp_view.html',{'result':data})
    
