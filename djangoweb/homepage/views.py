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
import uuid
from django.contrib.auth.models import User
from .models import Profile
from django.template import engines
from django.shortcuts import get_object_or_404
from .forms import RestaurantForm
from .models import Restaurant



@login_required
def index(request):
    now = timezone.now()
    template_string = """
     {% extends "homepage/base.html" %}
     {% block title %}Welcome{% endblock %}
     {% block content %}
       <div class="container text-center mt-5">
                <h1>Hello! I am {{ request.user.username }} 🌍</h1>
                <p>Current time and date: <b>{{ now|date:"Y-m-d H:i:s" }}</b></p>
            </div>
            {% endblock %}
    """
    template = engines['django'].from_string(template_string)
    return HttpResponse(template.render({'now': now}, request))

# ------------------ SIGNUP VIEW ------------------
def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            #user.username = str(uuid.uuid4())[:30]  # fits Django username length save username

            user.save()
            gender = form.cleaned_data.get('gender')
            birthday = form.cleaned_data.get('birthday')
            Profile.objects.create(user=user, gender=gender, birthday=birthday)
            login(request, user)
           
            messages.success(request, '✅ Your account has been created successfully!')
            
           
            return redirect('login')  # Redirect to homepage or dashboard
        else: 
            messages.error(request, '❌ Please correct the errors below.')
    else:
             form = SignupForm() 
    return render(request, 'homepage/signup.html', {'form': form})

# ------------------ LOGIN VIEW ------------------
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # get the UUID username from email
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            username = None

        if username:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                 return redirect(next_url) 
                return redirect('index')  # change 'home' to your homepage URL name
        messages.error(request, 'Invalid email or password')
    return render(request, 'homepage/login.html')





# ------------------ LOGOUT VIEW ------------------
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, '✅ You have been logged out successfully.')
    return redirect('login')

@login_required
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
@login_required
def success_view(request):
    """Simple success page after form submission."""
    return render(request, "homepage/success.html")

@login_required
def product_view(request):
    """Display the Product form and handle submission."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = ProductForm(request.POST, instance=product)
            form.save()
            return HttpResponse("<h2>Product saved successfully!</h2>")
    else:
        form = ProductForm()

    return render(request, "homepage/product_form.html", {'form': form})

#------------Manage product--------------
@login_required
def manage_products(request):
    """List all products with action buttons."""
    products = Product.objects.all().order_by('id')
    return render(request, 'homepage/manage_products.html', {'products': products})


@login_required
def product_create(request):
    """Create a new product."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Product has been saved successfully!')
            return redirect('manage_products')
        else:
            print(form.errors)
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = ProductForm()
    return render(request, 'homepage/product_form.html', {'form': form, 'title': 'Create Product'})


@login_required
def product_update(request, pk):
    """Edit an existing product."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Product has been updated successfully!')
            return redirect('manage_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'homepage/product_form.html', {'form': form, 'title': 'Edit Product'})


@login_required
def product_delete(request, pk):
    """Delete a product."""
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, '✅ Product deleted successfully!')
    return redirect('manage_products')



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

#-----------Restaurant------------#
@login_required
def manage_restaurants(request):
    """List all restaurants."""
    restaurants = Restaurant.objects.all().order_by('id')
    return render(request, 'homepage/manage_restaurants.html', {'restaurants': restaurants})

@login_required
def restaurant_create(request):
    """Create a new restaurant."""
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Restaurant has been saved successfully!')
            return redirect('manage_restaurants')
    else:
        form = RestaurantForm()
    return render(request, 'homepage/restaurant_form.html', {'form': form, 'title': 'Create Restaurant'})

@login_required
def restaurant_update(request, pk):
    """Edit an existing restaurant."""
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Restaurant has been updated successfully!')
            return redirect('manage_restaurants')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'homepage/restaurant_form.html', {'form': form, 'title': 'Edit Restaurant'})

@login_required
def restaurant_delete(request, pk):
    """Delete a restaurant."""
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()
    messages.success(request, '✅ Restaurant deleted successfully!')
    return redirect('manage_restaurants')