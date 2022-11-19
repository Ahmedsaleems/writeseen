import os
from django.db import models
from user.models import User
from uuid import uuid4
from PIL import Image

def path_and_rename(instance, filename):
    upload_to = 'userpics'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

# Create your models here.
class UserProfileIndustry(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to=path_and_rename, max_length=264, null=True, blank=True)
    phone_number = models.PositiveIntegerField(default=0,null=True, blank=True)
    organization_name = models.CharField(max_length=200,null=True,blank=True)
    industry = models.CharField(max_length=100,null=True,blank=True)
    profession = models.CharField(max_length=100,null=True,blank=True)
    company_email = models.EmailField(max_length=100,null=True,blank=True)
    company_phone_number = models.PositiveIntegerField(default=0,null=True, blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    shelf = models.BooleanField(default=False)
    write_chat = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        instance = super(UserProfileIndustry, self).save(*args, **kwargs)
        if self.profile_pic:
            image = Image.open(self.profile_pic.path)
            image.save(self.profile_pic.path,quality=20,optimize=True)
        return instance
    
    def __str__(self):
        return str(self.user.username)

class IAM(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class UserProfileWriter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to=path_and_rename, max_length=264, null=True, blank=True)
    phone_number = models.PositiveIntegerField(default=0,null=True, blank=True)
    about_me = models.TextField()
    country = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    shelf = models.BooleanField(default=False)
    write_chat = models.BooleanField(default=False)
    iam = models.ManyToManyField(IAM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        instance = super(UserProfileWriter, self).save(*args, **kwargs)
        if self.profile_pic:
            image = Image.open(self.profile_pic.path)
            image.save(self.profile_pic.path,quality=20,optimize=True)
        return instance
    
    def __str__(self):
        return str(self.user.username)    