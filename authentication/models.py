from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        """ Return string representation of our user """
        return self.email