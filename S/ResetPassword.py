#registration/login.html
<!-- registration/login.html -->
<form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
<p><a href="{% url 'password_reset' %}">Forgot password?</a></p>

#registration/password_reset_form.html
<form method="post">
    {% csrf_token %}
    <label for="username">Username:</label>
    <input type="text" name="username" id="username" required>
    <button type="submit">Reset Password</button>
</form>

#registration/password_reset_confirm.html
{% if form %}
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Set New Password</button>
</form>
{% else %}
<p>The reset link is invalid or has expired.</p>
{% endif %}

#registration/password_reset_complete.html
<p>Your password has been set. You can now <a href="{% url 'login' %}">log in</a> with the new password.</p>


#project/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import login

# 显示密码重置请求表单
def password_reset_request_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            return redirect('password_reset_confirm', uidb64=uid, token=token)
    return render(request, 'registration/password_reset_form.html')

# 显示密码重置确认表单
def password_reset_confirm_view(request, uidb64=None, token=None):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                login(request, user)
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
    else:
        form = None

    return render(request, 'registration/password_reset_confirm.html', {'form': form})

# 显示密码重置完成确认页面
def password_reset_complete_view(request):
    return render(request, 'registration/password_reset_complete.html')


#urls.py
from django.urls import path
from .views import password_reset_request_view, password_reset_confirm_view, password_reset_complete_view

urlpatterns = [
    path('accounts/password_reset/', password_reset_request_view, name='password_reset'),
    path('accounts/reset/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
    path('accounts/reset/done/', password_reset_complete_view, name='password_reset_complete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # 确保登录视图也在此配置中
]




