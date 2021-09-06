from django.shortcuts import render

from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from blogapp.forms import ModeForm
from blogapp.models import blog


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('demo')
        else:
            messages.info(request,'invalid details')
            return redirect('/')


    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()
                print("user created")
        else:
            print("password not matched")
        return redirect('login')
    else:
        return render(request, 'reg.html')

def add_blog(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        s = blog(name=name, desc=desc, image=image)
        s.save()
        print('product added')
    return render(request, 'add.html')

def detail(request,blog_id):
    items=blog.objects.get(id=blog_id)
    return render(request,'detail.html',{'item':items})

def demo(request):
    items= blog.objects.all()
    return render(request,"home.html",{'items':items})


def update(request, id):
    obj = blog.objects.get(id=id)
    form = ModeForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'obj': obj})

def delete(request, id):
    if request.method == 'POST':
        obj = blog.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request, 'delete.html')
