from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import UserInfoForm, ProductForm  # Added ProductForm
from .models import UserInfo, Product  # Added Product

# ------------------ Existing index view ------------------
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

# ------------------ User Form Views ------------------
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


# ------------------ New Product Form View ------------------
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
