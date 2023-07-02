from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from demoapp.forms import Loginform, Userloginform, productaddform
from demoapp.models import userlogin, productadd


# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    form = Loginform()
    form1 = Userloginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        form1 = Userloginform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            tcr = form1.save(commit=False)
            tcr.user = user
            tcr.save()
            return redirect('loginview')
    return render(request,'registration.html',{'form':form,'form1':form1})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('adminhome')

        if user is not None and user.is_user:
            login(request,user)
            return redirect('userhome')

        else:
            messages.info(request,'Invalid credentials')
    return render(request,'login.html')

def adminhome(request):
    return render(request,'admin/dash.html')

def userhome(request):
    return render(request,'user/dash.html')

def userprofileview(request):
    u = request.user
    data = userlogin.objects.filter(user=u)
    print(data)
    return render(request,'user/profileview.html',{'data':data})

def profileupdate(request,id):
    profile = userlogin.objects.get(id=id)
    form1 = Userloginform(instance=profile)
    if request.method == 'POST':
        form = Loginform(request.POST or None,instance=profile or None)
        # form1 = userloginform(request.POST or None,request.FILES,instance=profile or None)
        form1 = Userloginform(request.POST or None,request.FILES,instance=profile or None)
        if form1.is_valid():
            user = form1.save(commit=True)
            user.is_teacher = True
            user.save()
        return redirect('userprofileview')

    return render(request,'user/profileupdate.html',{'form1':form1})

def addproduct(request):
    form = productaddform()
    u = request.user
    if request.method=='POST':
        form = productaddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewproduct')
    return render(request,'admin/addproduct.html',{'form':form})

def viewproduct(request):
    u = request.user
    data = productadd.objects.all()
    return render(request,'admin/viewproduct.html',{'data':data})

def updateproduct(request,id):
    user = productadd.objects.get(id=id)
    form = productaddform(instance=user)
    if request.method == "POST":
        form = productaddform(request.POST or None, request.FILES, instance=user or None)
        if form.is_valid():
            prd = form.save(commit=False)
            prd.save()
            return redirect('viewproduct')
    return render(request, 'admin/updateproduct.html', {'form': form})

def deleteproduct(request,id):
    data=productadd.objects.get(id=id)
    data.delete()
    return redirect('viewproduct')

def userviewproduct(request):
    u = request.user
    data = productadd.objects.all()
    return render(request,'user/userviewproducts.html',{'data':data})
