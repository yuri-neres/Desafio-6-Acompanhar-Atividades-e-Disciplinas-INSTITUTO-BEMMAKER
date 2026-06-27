from django.shortcuts import render

def index_professor(request):
    return render(request, 'professores/index.html')