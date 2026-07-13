from django.shortcuts import render
from core.decorators import professor_required

@professor_required
def index_professor(request):
    return render(request, 'professores/index.html')