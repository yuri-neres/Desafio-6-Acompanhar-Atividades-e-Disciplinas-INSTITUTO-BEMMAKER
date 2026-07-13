from django.http import HttpResponseForbidden
from functools import wraps


def aluno_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('login')

        if request.user.groups.filter(name='Alunos').exists() or request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        return HttpResponseForbidden("Você não tem permissão para acessar esta página. Área exclusiva para alunos.")

    return _wrapped_view

    
def professor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('login')

        if request.user.groups.filter(name='Professores').exists() or request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        return HttpResponseForbidden("Você não tem permissão para acessar esta página. Área exclusiva para professores.")

    return _wrapped_view