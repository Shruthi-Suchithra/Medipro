from django.shortcuts import render,redirect
from .models import usersinfo
from admin_app.views import *
from .models import doctorsinfo
from .models import appointmentsinfo


# Create your views here.
def user_register(request):
    if request.method == "POST":

        # (photo,name,... variable names)
        # media is used  in post
        photo=request.FILES.get('photo')
        # get is used in name,email...

        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        data=usersinfo(photo=photo,name=name,email=email,phone=phone,password=password)
        data.save()
    return render(request,'signup.html') 
def user_login(request):
    if request.method == "POST":
        useremail=request.POST.get('email')
        userpassword=request.POST.get('password')


        if useremail == "admin@gmail.com" and userpassword == "admin":
            request.session['email'] = useremail
            request.session['admin'] = 'admin'
            return render(request,'index.html') 
        
        elif usersinfo.objects.filter(email=useremail, password=userpassword).exists():

            userdetails = usersinfo.objects.get(
                email=useremail,
                password=userpassword
            )

            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.name
            request.session['uemail'] = userdetails.email
            request.session['user'] = 'user'
            return render(request,'index.html') 


    return render(request,'login.html')   

# login form

def logout(request):
    session_keys = list(request.session.keys())
    # current details in session keys method
    for key in session_keys:
        # delete for using loop 
        del request.session[key]
    return redirect(index)   
# admin app function name (index)
# redirect is used for new request creating 


def userprofile(request):
    userid=request.session['uid']
    data=usersinfo.objects.get(pk=userid)
    # primary key 
    return render(request,'userprofile.html',{'result':data})
# result is a string 


def userupdate(request,id):
    data=usersinfo.objects.get(pk=id)
    return render(request,'userupdate.html',{'result':data})


def userupdates(request,id):
    if request.method=="POST":
        photo=request.FILES.get("photo")
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        data=usersinfo(id=id,photo=photo,name=name,email=email,phone=phone,password=password)
        data.save()
        return redirect(userview)
    return render(request,'userupdate.html')

# doctor register


def doc_register(request):
    if request.method == "POST":

        # (photo,name,... variable names)
        # media is used  in post
        # photo=request.FILES.get('photo')
        # get is used in name,email...

        docphoto=request.FILES.get('docphoto')
        docname=request.POST.get('docname')
        docspecialization=request.POST.get('docspecialization')
        docpayment=request.POST.get('docpayment')
        doctiming=request.POST.get('doctiming')
        data=doctorsinfo(docphoto=docphoto,docname=docname,docspecialization=docspecialization,docpayment=docpayment,doctiming=doctiming)
        data.save()
    return render(request,'doctorreg.html.') 

def doctorupdate(request,id):
    data=doctorsinfo.objects.get(pk=id)
    return render(request,'doctorupdate.html',{'result':data})

def doctorupdates(request,id):
    if request.method=="POST":
        docphoto=request.FILES.get("docphoto")
        docname=request.POST.get("docname")
        docspecialization=request.POST.get("docspecialization")
        docpayment=request.POST.get("docpayment")
        doctiming=request.POST.get("doctiming")
        data=doctorsinfo(id=id,docphoto=docphoto,docname=docname,docspecialization=docspecialization,docpayment=docpayment,doctiming=doctiming)
        data.save()
        return redirect(doctorview)
    return render(request,'doctorupdate.html')



# login 

def bookapp(request):
    userid=request.session['uid']
    docdet=doctorsinfo.objects.all()
    if request.method=='POST':
        patientname=request.POST.get("patientname")
        patientage=request.POST.get("patientage")
        patientemail=request.POST.get("patientemail")
        patientphone=request.POST.get("patientphone")
        docname=request.POST.get("docname")
        bookingdate=request.POST.get("bookingdate")
        patientproblem=request.POST.get("patientproblem")
        data=appointmentsinfo(userid=userid,patientname=patientname,patientage=patientage,patientemail=patientemail,patientphone=patientphone,patientproblem=patientproblem,docname=docname,bookingdate=bookingdate)
        data.save()
    return render(request,'appointment.html',{'result':docdet})

def appointment_view(request):
    userid=request.session['uid']
    data=appointmentsinfo.objects.filter(userid=userid)
    return render(request,'appointment_view.html',{'result':data})
def appointmentdelete(request,id):
    data=appointmentsinfo.objects.get(pk=id)
    data.delete()
    return redirect(bookapp)




        
