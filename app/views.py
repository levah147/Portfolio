from django.shortcuts import render,redirect
from django.http import FileResponse, Http404
from django.conf import settings
import os
from django.contrib import messages
from .forms import ContactForm


def download_cv(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv/mycv.pdf')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='MyCV.pdf')
    raise Http404("CV not found")





def index(request):
    return render(request, 'core/index.html')

# def about(request):
#     return render(request, 'core/about.html')

# def services(request):
#     return render(request, 'core/services.html')

def skill(request):
    return render(request, 'core/skills.html')
    
# def teams(request):
#     return render(request, 'core/teams.html')



def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data to the database
            messages.success(request, "Thank you for your message! We'll get back to you soon.")
            return redirect('contact')
        else:
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})



# def hire(request):
#     return render(request,'hire.html')