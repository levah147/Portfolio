from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def skills(request):
    return render(request, 'core/skills.html')
    
def teams(request):
    return render(request, 'core/teams.html')

def contact(request):
    return render(request, 'core/contact.html')

def hire(request):
    return render(request,'hire.html')