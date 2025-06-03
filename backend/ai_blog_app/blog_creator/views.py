from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    return render(request, 'login.html')

def user_logout(request):
    pass

def user_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('confirmPassword')

        if password == repeat_password:
            try:
                user = User.objects.create_user(
                    email,
                    password
                )
                user.save()
                # Automatically log in the user after signup
                login(request, user)
                return redirect('index') # Redirect to index view (not template.html) after successful signup
            except Exception as e:
                error_message = f"An error occurred during account creation: {str(e)}"
                return render(request, 'user_signup', {'error': error_message})
        else:
            error_message = "Passwords do not match."
            return render(request, 'user_signup', {'error': error_message})

    return render(request, 'signup.html')