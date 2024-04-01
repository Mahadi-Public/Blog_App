from django.urls import path
from authentication.views import LoginPageView, SingupPageView, ActivateAccountView, LogoutPageView,PasswordChangedView, PasswordResetView,ForgetPasswordView,ForgetPasswordDoneView,ForgetPasswordConfirmView,ForgetPasswordCompleteView

urlpatterns = [
    path('', LoginPageView.as_view(), name='LoginPageView'),
    path('signup/', SingupPageView.as_view(), name='SingupPageView'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activateAccountView'),
    path('logout/', LogoutPageView.as_view(), name='LogoutPageView'),
    path('password-changed/', PasswordChangedView.as_view(), name='PasswordChangedView'),
    
    path('reset-password/',ForgetPasswordView.as_view(), name='password_reset'),
    path('reset-password-done/',ForgetPasswordDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',ForgetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-done/',ForgetPasswordCompleteView.as_view(), name='password_reset_complete'),
]
