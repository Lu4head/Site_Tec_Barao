from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def dash(request):
    if not request.user.is_superuser: # Apenas usuários logados e administrativos podem entrar na pagina da dashboard
        messages.error(request,'Apenas usuários ADMINISTRATIVOS podem acessar a dashboard')
        return redirect('/')
    else:
        # Dashboard

        return render(request, 'dashboards/dashboards.html')