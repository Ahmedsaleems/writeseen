from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Content)
admin.site.register(ContentMaster)
admin.site.register(TagsMaster)
admin.site.register(GenrMaster)
admin.site.register(LanguageMaster)
admin.site.register(TypeMaster)
admin.site.register(AuthorMaster)
