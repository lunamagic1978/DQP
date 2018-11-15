from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def api_home(request):
    username = request.session.get('username')
    namespace_list = ApiNameSpace.objects.all()

    ctx = {"username": username,
           "namespace_list": namespace_list}
    return render(request, 'api-home.html', ctx)