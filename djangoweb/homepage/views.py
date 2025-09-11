from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import UserInfoForm  # Make sure forms.py exists with UserInfoForm

# Existing index view
def index(request):
    now = timezone.now()
    html = f"""
    <html>
        <head><title>Welcome</title></head>
        <body style="display:flex; justify-content:center; align-items:center; height:100vh; font-size:24px; background:#f4f4f4;">
            <div>
                <h1>Hello! 🌍</h1>
                <p>Current time and date: <b>{now.strftime('%Y-%m-%d %H:%M:%S')}</b></p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)

# ---------- New Bootstrap form views ----------

def user_info_view(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserInfoForm()
    return render(request, "homepage/user_form.html", {'form': form})

def success_view(request):
    return render(request, "homepage/success.html")
