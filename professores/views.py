from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index_professor(request):
    return render(request, 'professores/index.html')