from django.http import HttpResponse
from django.utils import timezone

def home(request):
    now = timezone.now()
    html = f"""
    <html>
      <head>
        <title>My Web Page</title>
        <style>
          body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f8ff;
            font-family: Arial, sans-serif;
          }}
          .box {{
            text-align: center;
            padding: 30px;
            border-radius: 15px;
            background: white;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
          }}
          h1 {{ color: #0077b6; }}
          p {{ font-size: 18px; }}
        </style>
      </head>
      <body>
        <div class="box">
          <h1>🌟 Welcome to My Page 🌟</h1>
          <p>Current Date & Time:</p>
          <h2>{now.strftime('%Y-%m-%d %H:%M:%S')}</h2>
        </div>
      </body>
    </html>
    """
    return HttpResponse(html)
