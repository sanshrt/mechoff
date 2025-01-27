from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegisterForm
from .models import Register

# Home page view
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user})
    else:
        return redirect('login')  # Redirect to login page if the user is not logged in

# Registration view
def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form if it is valid
            messages.success(request, 'Registration successful!')
            return redirect('login')  # Redirect to login page after successful registration
        else:
            # If the form is not valid, re-render the form with error messages
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()  # Instantiate the form
        return render(request, 'register.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')  # Email ID (username)
        password = request.POST.get('password')

        # Authenticate using Django's built-in authenticate method
        user = authenticate(username=user_name, password=password)

        if user is not None:
            auth_login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login')  # Stay on the login page if authentication fails

    return render(request, 'login.html')

# Logout view
def logout_view(request):
    auth_logout(request)  # Log the user out
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')  # Redirect to home page after logout
