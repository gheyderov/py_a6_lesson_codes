from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import ContactForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

def contact(request):
    form = ContactForm()
    print('get')
    if request.method == 'POST':
        print('POST')
        form = ContactForm(data = request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            messages.add_message(request, messages.SUCCESS, "Successfully sent!")
            return redirect(reverse_lazy('contact'))
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)