from django.shortcuts import render,redirect
import os
from django.conf import settings
from django.http import FileResponse, Http404

def download_cv(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv/mycv.pdf')
    # Debug: Log or print the file_path to verify it's correct
    print("Looking for CV at:", file_path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='MyCV.pdf')
    else:
        raise Http404("CV not found")





# def index(request):
#     return render(request, 'core/index.html')

# def about(request):
#     return render(request, 'core/about.html')

# def services(request):
#     return render(request, 'core/services.html')

def skill(request):
    return render(request, 'core/skills.html')
    
# def teams(request):
#     return render(request, 'core/teams.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the submission to the database
            messages.success(request, "Your message has been sent successfully!")
            return redirect('/')  # Redirect to a 'thank you' page or reload form
        else:
            messages.error(request, "There was an error in your form. Please correct it and try again.")
    else:
        form = ContactMessageForm()
    
    return render(request, 'core/index.html', {'form': form})




# def hire(request):
#     return render(request,'hire.html')