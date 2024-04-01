import threading
from django.views import View
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from authentication.forms import LoginForm, SingupForm, ChangesPasswordForm, ForgetPasswordConfirmForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

UserModel = get_user_model()

class LoginPageView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'successfully login accounts')
                return redirect('PostListView')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field == '__all__':
                        messages.error(request, f"{field}: {error}")
        return render(request, 'auth/login.html', {'form': form})



class SingupPageView(View):
    def get(self, request):
        form = SingupForm()
        return render(request, 'auth/singup.html', {'form': form})
    
    def post(self, request):
        form = SingupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate Your Accounts'
            message = render_to_string('auth/sendmail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail = form.cleaned_data.get('email')
            email_thread = threading.Thread(target=self.send_mail, args=(mail_subject, message, [send_mail]))
            email_thread.start()
            messages.info(request, 'Activate your account from the mail you provided')
            return redirect('LoginPageView')
        return render(request, 'auth/singup.html', {'form': form})
    
    def send_mail(self, subject, messages, to):
        email = EmailMessage(subject,messages,to=to)
        email.send()



class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your account is activated, now you can login')
            return redirect('LoginPageView')
        else:
            messages.warning(request, 'activate link is invalid')
            return redirect('SingupPageView')

class LogoutPageView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        messages.success(request, 'Your account successfully logged out!')
        return redirect('LoginPageView')

class PasswordChangedView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = ChangesPasswordForm(user=request.user)
        return render(request, 'auth/password_change.html', {'form': form})
    
    @method_decorator(login_required)
    def post(self, request):
        form = ChangesPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            return redirect('PostListView')
        else:
            form = ChangesPasswordForm(user=request.user)
        return render(request, 'auth/password_change.html', {'form' : form})      


class ForgetPasswordView(PasswordResetView):
    template_name = 'auth/reset_password.html'
    
class ForgetPasswordDoneView(PasswordResetDoneView):
    template_name = 'auth/reset_password_done.html'


class ForgetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'auth/reset_password_confirm.html'    
    form_class = ForgetPasswordConfirmForm   
    

class ForgetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'auth/reset_password_complete.html'