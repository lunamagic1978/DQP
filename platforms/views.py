from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth



@login_required
def index(request):
    username = request.session.get('username')
    ctx = {"username": username}
    # return render(request, 'index.html', ctx)
    return HttpResponseRedirect('/api/home')


def login_page(request):
    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect('/index')
        else:
            ctx = {"error_msg": "账号或者密码不正确"}
            return render(request, 'login.html', ctx)
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index')