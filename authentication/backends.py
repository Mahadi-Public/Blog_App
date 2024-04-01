from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to fetch user by email
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                # Try to fetch user by username
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None
        
        # If user is found, check the password
        if user.check_password(password):
            return user
        return None
