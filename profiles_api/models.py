from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.

class UserProfileManager(BaseUserManager):
    '''Manager For User Profile'''

    def create_user(self, email, name, password=None):
        '''Create a New User Profile'''
        if not email:
            raise ValueError("User Must Have an Valid Email Address...")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        '''Create and Save New SuperUser with given details'''
        user = self.create_user(email, name, password) #No need to pass self it will be passed automatically

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):

    ''' Database Model For User in the System '''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Retrive Full Name of User'''
        return self.name

    def get_short_name(self):
        '''Retrive Short Name of User'''
        return self.name

    def __str__(self):
        '''Returns String Representation of User'''
        return self.email


class ProfileFeedItem(models.Model):
    """Profile Status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
        )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the Model as String"""
        return self.status_text
