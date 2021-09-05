from django.shortcuts import render, redirect
from .forms import ContactModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def contact(request):
	return render(request, 'contact.html')