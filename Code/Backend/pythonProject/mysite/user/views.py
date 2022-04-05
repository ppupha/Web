from django.shortcuts import render, redirect
from user.forms import UserInfoForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
#from task.views import make_noti
#from task.models import Task, Project, Notification
import sys
sys.path.append('../')
from product.models import Profile


class IndexView(View):
    def get(self, request):
        return render(request, 'user/index.html')

class HelpView(View):
    def get(self, request):
        return render(request, 'user/help.html')

class AuthorsView(View):
    def get(self, request):
        return render(request, 'user/authors.html')


@login_required
def user_logout(request):
    logout(request)
    request.session.flush()
    return redirect('home:home')

'''
@login_required(login_url='/login/')
def user_profile(request):
    # Add notification to navbar
    #make_noti(request)
    projects = request.user.project_set.all()
    tasks = Task.objects.filter(project__in = list(projects))
    notis = Notification.objects.filter(task__in = list(tasks)).order_by('-id')
    notic_count = len(list(Notification.objects.filter(actived = False)))
    
    # Form edit profile
    form = UserInfoForm(instance=request.user.Info)
    
    data = {"notis": notis, 'form': form, "notic_count": notic_count}
    
    if request.method == "POST":
        form = UserInfoForm(request.POST, request.FILES, instance=request.user.Info)
        if form.is_valid():
            custom_form = form.save(False)
            custom_form.user = request.user
            custom_form.save()
            return redirect('user:user_profile')
        
    return render(request, 'user/user_profile.html', data)
'''
class SignupView(View):
    """
    Load signup page
    If success == 1 then return successful registration message
    else return registration form
    """
    def get(self, request):
        user_form = UserForm()
        return render(request, 'user/signup.html', {'user_form': user_form, 'success': 0})

    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():

            user = user_form.save(commit=False)
            user.is_active = True
            user.save()

            #profile = Profile.objects.create(user = user)
            #profile.save()
            return render(request, 'user/signup.html', {'user_form': user_form, 'success': 1,})
        return render(request, 'user/signup.html', {'user_form': user_form, 'success': 0, })


class LoginClass(View):
    """
    Load login page
    If user is authenticated then redirect to task:projects page
    else return the corresponding errors
    - Password is not correct
    - Account is inactive
    - Username does not exist
    """
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:home')
        return render(request, 'user/login.html', {'mode': 0})

    def post(self, request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        # return a user if both username and password are valid

        user = authenticate(username=user_name, password=pass_word)
        if user:
            if user.is_active or True:
                login(request, user)
                return redirect('home:home')
        else:
            user = User.objects.filter(username=user_name)
            return render(request, 'user/login.html', {'user': user, 'mode': 1})


class ActivateView(View):

    def get(self, request, uidb64, token):
        try:
            # Decode a base64 encoded string. The received data is a user's primary key
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        # if user exists and check_token is correct then account is successful activated
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('home:home')
        else:
            return render(request, 'registrations/acc_active_invalid.html')


class PasswordChangeView_(auth_views.PasswordChangeView):
    success_url = reverse_lazy('user:password_change_done')
    template_name = 'registrations/password_change_form.html'


class PasswordChageDoneView_(auth_views.PasswordChangeDoneView):
    template_name = 'registrations/password_change_done.html'


class PasswordResetView_(auth_views.PasswordResetView):
    subject_template_name = 'registrations/password_reset_subject.txt'
    template_name = 'registrations/password_reset_form.html'
    success_url = reverse_lazy('user:password_reset_done')
    email_template_name = 'registrations/password_reset_email.html'
    html_email_template_name = email_template_name


class PasswordResetDoneView_(auth_views.PasswordResetDoneView):
    template_name = 'registrations/password_reset_done.html'


class PasswordResetConfirmView_(auth_views.PasswordResetConfirmView):
    template_name = 'registrations/password_reset_confirm.html'
    success_url = reverse_lazy('user:password_reset_complete')


class PasswordResetCompleteView_(auth_views.PasswordResetCompleteView):
    template_name = 'registrations/password_reset_complete.html'
