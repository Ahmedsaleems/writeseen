import os
from django.db import models
from user.models import User
from uuid import uuid4
from PIL import Image

# Create your models here.
def path_authors(instance, filename):
    upload_to = 'authors'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_content(instance, filename):
    upload_to = 'content'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class ContentMaster(models.Model):
    content_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content_name)

class TagsMaster(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.tag_name)

class GenrMaster(models.Model):
    genr_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.genr_name)

class LanguageMaster(models.Model):
    lang_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lang_name)

class TypeMaster(models.Model):
    type_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.type_name)

class AuthorMaster(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    author_url = models.ImageField(upload_to=path_authors, max_length=264, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        instance = super(AuthorMaster, self).save(*args, **kwargs)
        if self.author_url:
            image = Image.open(self.author_url.path)
            image.save(self.author_url.path,quality=20,optimize=True)
        return instance
    
    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)

#GENR_CHOICES = (
 #    ("Drama", "Drama"),
  #   ("Comedy", "Comedy"),
   #  ("Horer", "Horer"),
   #  ("Action", "Action"),
   #  ("Fantasy", "Fantasy"),
   #  ("Animated", "Animated"),
   #  ("Other", "Other"),
   #  )

#LANGUAGE_CHOICES = (
    # ("English", "English"),
    # ("Espanol", "Espanol"),
    # ("Italiano", "Italiano"),
    # ("Deutsch", "Deutsch"),
    # ("Arabic", "Arabic"),
    # ("Francais", "Francais"),
    # ("Norsk", "Norsk"),
 #)

#TYPE_CHOICES = (
  #   ("Farce", "Farce"),
  #   ("Comedy Play", "Comedy Play"),
  #   ("One Act Play", "One Act Play"),
  #  ("Royalty Free Play", "Royalty Free Play"),
  #  ("All Male Play", "All Male Play"),
  #   ("All Female Play", "All Female Play"),
  #   ("Others", "Others"),
 #)

class Content(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    content_url = models.ImageField(upload_to=path_content, max_length=264, null=True, blank=True)
    #type = models.CharField(max_length=100,choices=TYPE_CHOICES, null=True, blank=True)
    #genr = models.CharField(max_length=100,choices=GENR_CHOICES, null=True, blank=True)
    #language = models.CharField(max_length=100,choices=LANGUAGE_CHOICES, null=True, blank=True)
    content_fro = models.ForeignKey(ContentMaster,on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(TypeMaster,on_delete=models.SET_NULL, null=True, blank=True)
    genr = models.ForeignKey(GenrMaster,on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(LanguageMaster,on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    write_line = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()
    author = models.ManyToManyField(AuthorMaster)
    tags = models.ManyToManyField(TagsMaster)
    attachment = models.FileField(upload_to=path_content, max_length=264, null=True, blank=True)
    youtube_link = models.CharField(max_length=265, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        instance = super(Content, self).save(*args, **kwargs)
        if self.content_url:
            image = Image.open(self.content_url.path)
            image.save(self.content_url.path,quality=20,optimize=True)
        return instance
    
    def __str__(self):
        return str(self.title)
