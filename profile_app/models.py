from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """ Manager for user's profile """

    def create_user(self, password=None, **kwargs):
        """ Create new user profile """
        if not kwargs.get('email'):
            raise ValueError('Kindly provide and email address')
        email = self.normalize_email(kwargs.get('email'))
        user = self.model(email=kwargs.get('email'), name=kwargs.get('name'))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None, **kwargs):
        superuser = self.create_user(password=None, **kwargs)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save(using=self._db)
        return superuser


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve fullname of the user """
        return self.name

    def get_short_name(self):
        """ Retrieve short name of user """
        return self.name

    def __str__(self):
        """ Return string representation of the model """
        return f'<UserProfile {self.email}>'
