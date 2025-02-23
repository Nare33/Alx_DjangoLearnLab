# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Custom Login View (Django built-in)
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Custom Logout View (Django built-in)
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

