from django.shortcuts import render, redirect
from app.models import ContactUs
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')
def product(request):
    return render(request, 'product.html')
def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        message = request.POST.get("message")
        if not email or not name or not message:
            messages.error(request, "All fields are required")
            return redirect(contact)
        ContactUs.objects.create(
            name=name, 
            email=email,
            message=message
        )
        messages.success(request, "Message sent")
        return redirect(home)
    return render(request, 'contact.html')