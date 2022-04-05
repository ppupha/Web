from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('accounts/password_reset/', views.PasswordResetView_.as_view(), name='password_reset'),
    path('accounts/reset/<uidb64>/<token>/', views.PasswordResetConfirmView_.as_view(), name='password_reset_confirm'),
    path('accounts/password_reset/done/', views.PasswordResetDoneView_.as_view(), name='password_reset_done'),
    path('accounts/reset/done/', views.PasswordResetCompleteView_.as_view(), name='password_reset_complete'),
    path('accounts/password_change/', views.PasswordChangeView_.as_view(), name='password_change'),
    path('accounts/password_change/done/', views.PasswordChageDoneView_.as_view(), name='password_change_done'),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
    #path('profile/', views.user_profile, name='user_profile'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('authors/', views.AuthorsView.as_view(), name='authors'),
    path('logout', views.user_logout, name='logout')
]
