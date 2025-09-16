from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignupForm, UserInfoForm, ProductForm
from django.contrib.auth.forms import AuthenticationForm
from .models import UserInfo, Product
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def index(request):
    now = timezone.now()
    html = f"""
    <html>
        <head><title>Welcome</title></head>
        <body style="display:flex; justify-content:center; align-items:center; height:100vh; font-size:24px; background:#f4f4f4;">
            <div>
                <h1>Hello! I am Rodu Sultan Jhang 🌍</h1>
                <p>Current time and date: <b>{now.strftime('%Y-%m-%d %H:%M:%S')}</b></p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)

# ------------------ SIGNUP VIEW ------------------
def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '✅ Your account has been created successfully!')
            
           
            return redirect('login')  # Redirect to homepage or dashboard
        elif form.errors:
            messages.error(request, '❌ Please correct the errors below.')
        else:
             form = SignupForm() 
    return render(request, 'homepage/signup.html', {'form': form})

# ------------------ LOGIN VIEW ------------------
def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'✅ Welcome back, {user.first_name}!')
            return redirect('home')
        else:
            messages.error(request, '❌ Invalid email or password.')
    return render(request, 'homepage/login.html', {'form': form})

# ------------------ LOGOUT VIEW ------------------
def logout_view(request):
    logout(request)
    messages.success(request, '✅ You have been logged out successfully.')
    return redirect('login')

def user_info_view(request):
    """Display the user form and handle submission. Includes link to show all records."""
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserInfoForm()

    # Check if URL has ?show=1 to display records table
    show_table = request.GET.get("show", "")
    users = UserInfo.objects.all() if show_table else None

    return render(request, "homepage/user_form.html", {
        'form': form,
        'users': users
    })

def success_view(request):
    """Simple success page after form submission."""
    return render(request, "homepage/success.html")


def product_view(request):
    """Display the Product form and handle submission."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Product saved successfully!</h2>")
    else:
        form = ProductForm()

    return render(request, "homepage/product_form.html", {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')
