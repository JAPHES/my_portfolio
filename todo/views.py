from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(subject, body, email, ['japhesmurithi@gmail.com'])

            return redirect('success')

    else:
        form = ContactForm()
        # Always return an HttpResponse
        return render(request, 'contact.html', {'form': form})
def success(request):
    return render(request, 'success.html')
#def gallery(request):
    #return render(request, 'gallery.html')  # Render the gallery template

def cv_page(request):
    return render(request, 'cv_page.html')


