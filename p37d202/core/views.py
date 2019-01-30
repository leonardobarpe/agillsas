from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
def inicio(request):
	return render(request, 'core/inicio.html')