from django.urls import path
from . import views

app_name = 'login'
from . import views as login_views

urlpatterns = [
	path('login/', login_views.login_root, name='login_root'),
	path('login/success/', login_views.login_success, name='login_success'),
	path('login/fail/', login_views.login_fail, name='login_fail')
]