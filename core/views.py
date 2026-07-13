from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')

@login_required
def redirecionar_login(request):
    if request.user.groups.filter(name='Professores').exists():
        return redirect('/professores/')
    elif request.user.groups.filter(name='Alunos').exists():
        return redirect('/alunos/')
    
    return redirect('/')