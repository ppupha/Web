from django.shortcuts import render


# Create your views here.

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

def login_root(request):
	# Login form submitted?
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		if username and password:
			user = authenticate(username=username, password=password)

			# Login succeeded
			if user is not None:
				url = reverse(viewname="login:login_success", current_app="login")

				return HttpResponseRedirect(url)

		# Login failed
		url = reverse(viewname="login:login_fail", current_app="login")
		return HttpResponseRedirect(url)

	return render(request, 'login/login_root.html')

def login_success(request):
	return render(request, 'login/login_success.html')

def login_fail(request):
	return render(request, 'login/login_fail.html')