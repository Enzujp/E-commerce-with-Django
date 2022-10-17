from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from core.views import index
from .models import Userprofile
# Create your views here.

def vendor_detail(request, pk):
    user = User.objects.get(pk)

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user
    })
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('index')

    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })