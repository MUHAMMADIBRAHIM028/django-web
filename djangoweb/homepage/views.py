from django.http import HttpResponse
from django.utils import timezone

def index(request):
    now = timezone.now()
    html = f"""
    <html>
        <head><title>Welcome</title></head>
        <body style="display:flex; justify-content:center; align-items:center; height:100vh; font-size:24px; background:#f4f4f4;">
            <div>
                <h1>Hello Ibrahim This is my first website ! 🌍</h1>
                <p>Current time and date: <b>{now.strftime('%Y-%m-%d %H:%M:%S')}</b></p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)
from django.shortcuts import render


# Create your views here.
