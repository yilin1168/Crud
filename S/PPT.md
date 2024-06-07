```html
<!-- template.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Download PPT</title>
</head>
<body>
    <button id="downloadBtn">Download PPT</button>

    <script>
        document.getElementById('downloadBtn').addEventListener('click', function() {
            window.location.href = '/download-ppt/';
        });
    </script>
</body>
</html>

```


```python
#views.py
from django.http import HttpResponse
from django.conf import settings
import os

def download_ppt(request):
    file_path = os.path.join(settings.BASE_DIR, 'default', 'yourfile.pptx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
            response['Content-Disposition'] = 'attachment; filename="yourfile.pptx"'
            return response
    else:
        return HttpResponse("File not found.", status=404)


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('download-ppt/', views.download_ppt, name='download_ppt'),
]


```
