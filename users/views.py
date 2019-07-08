from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import MyUser
from . admin import UserCreationForm

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User has been successfully created')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def teacher_signup(request):
    if request.user.is_authenticated:
        pass
        # return redirect('/')
    else:

        if request.method == 'POST':
            email = request.POST.get('email')
            fullname = request.POST.get('fullname')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            formcheck = request.POST.get('formcheck')
            if password != password2:
                messages.warning(request, 'Password doesn\'t matched')
            else:
                try:

                # user = MyUser.objects.create( email=email, full_name=fullname, password=password, is_active=True, is_teacher=True,is_student=False,is_admin=False)
                    user = MyUser.objects.create_teacher( email=email, full_name=fullname, password=password)
                    return HttpResponse('Teacher has been created successfully')
                except:
                    messages.warning(request, 'Email adready exists')

    return render(request, 'users/teacher_signup.html', {})

def logoutviews(request):
    logout(request)
    return redirect('/')