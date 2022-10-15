from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def vendor_detail(request, pk):
    user = User.get.objects(pk=pk)

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user
    })