from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Mensaje enviado correctamente! Te contactaremos pronto.')
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact_form.html', {'form': form})
