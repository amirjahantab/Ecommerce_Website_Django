from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

def get_home_image_filepath(self, filename):
    return 'images/' + str(self.pk) + '/home_image.png'

def get_defult_image_filepath(self, filename):
    return 'images/' + str(self.pk) + '/defult_image.png'

def get_services_first_image_filepath(self, filename):
    return 'images/' + str(self.pk) + '/services_first_image.png'

def get_services_second_image_filepath(self, filename):
    return 'images/' + str(self.pk) + '/services_first_image.png'

def get_services_third_image_filepath(self, filename):
    return 'images/' + str(self.pk) + '/services_third_image.png'

class HomePage(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to= get_home_image_filepath, default=get_defult_image_filepath, blank=True, null=True)
    
    telegram_link = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    
    services = models.CharField(max_length=200, null=True, blank=True)
    services_description = models.TextField(null=True, blank=True)
    first_title_services = models.CharField(max_length=200, null=True, blank=True)
    first_image_services = models.ImageField(upload_to=get_services_first_image_filepath, null=True, blank=True)
    first_description_services = models.TextField(null=True, blank=True)
    second_title_services = models.CharField(max_length=200, null=True, blank=True)
    second_image_services = models.ImageField(upload_to=get_services_second_image_filepath, null=True, blank=True)
    second_description_services = models.TextField(null=True, blank=True)
    third_title_services = models.CharField(max_length=200, null=True, blank=True)
    third_description_services = models.TextField(null=True, blank=True)
    third_image_services = models.ImageField(upload_to=get_services_third_image_filepath, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return 'profile/profile_images' + str(self.pk) + '/profile_image.png'


def get_default_profile_image():
    return 'profile/profile_default/default_profile_image.png'


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(
        max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image
        )
    hide_email = models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()    
    
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # simplest possible answer: Yes, always
        return True