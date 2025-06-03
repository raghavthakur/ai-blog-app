from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def generate_blog(request):
    pass

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('index')  # Redirect to index view (not templates) after successful login
        else:
            error_message = "Invalid email or password."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('confirmPassword')

        if password == repeat_password:
            try:
                user = User.objects.create_user(
                    username=email,  # Use email as username
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                # Automatically log in the user after signup
                login(request, user)
                return redirect('index')
            except Exception as e:
                error_message = f"An error occurred during account creation: {str(e)}"
                return render(request, 'user_signup.html', {'error_message': error_message})
        else:
            error_message = "Passwords do not match."
            return render(request, 'user_signup.html', {'error_message': error_message})

    return render(request, 'signup.html')