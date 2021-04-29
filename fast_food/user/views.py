from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users
from .forms import UsersForm

def index(request):
    return HttpResponse('salom')

def sign(request):
    form = UsersForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid() and form.save():
            return HttpResponse('save')

    else:
        form = UsersForm()

    context = {
        'form': form
    }
    return render(request, 'sign_in.html', context)