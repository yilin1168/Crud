# views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('app.view_table2', login_url='/login/', raise_exception=True)
def my_view(request):
    return render(request, 'my_template.html')

def permission_denied_view(request, exception):
    return render(request, 'no_permission.html')


# middleware.py
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

class PermissionDeniedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied):
            return redirect('no_permission')
        return None
      
# settings.py
MIDDLEWARE = [
    # ... other middleware ...
    'your_app.middleware.PermissionDeniedMiddleware',
]

# settings.py
LOGIN_URL = '/login/'  # 修改为你的登录页面URL


# urls.py
from django.urls import path
from .views import my_view, permission_denied_view

urlpatterns = [
    path('my_view/', my_view, name='my_view'),
    path('no_permission/', permission_denied_view, name='no_permission'),
]


#no permission.html
<!-- no_permission.html -->
<!DOCTYPE html>
<html>
<head>
    <title>No Permission</title>
</head>
<body>
    <h1>No Permission</h1>
    <p>You do not have the required permission to view this page.</p>
</body>
</html>


