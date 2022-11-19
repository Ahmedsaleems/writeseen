"""WriteSeen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from userprofile import views as user_profile_view
from content import views as content_view
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Write Seen')

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'account-writer', user_profile_view.UserProfileWriterViewSet)
router.register(r'account-industry', user_profile_view.UserProfileIndustryViewSet)
router.register(r'user-detail', user_profile_view.UserBasicInformationViewSet)
router.register(r'iam', user_profile_view.WhoIamUserWriterViewSet)
router.register(r'author', content_view.AuthorMasterViewSet)
router.register(r'content-fro', content_view.ContentMasterViewSet)
router.register(r'tags', content_view.TagsViewSet)
router.register(r'genr', content_view.GenrMasterViewSet)
router.register(r'type', content_view.TypeMasterViewSet)
router.register(r'language', content_view.LanguageMasterViewSet)
router.register(r'content', content_view.ContentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^$', schema_view),
    path('', include(router.urls)),
    path('api/user/',include('user.urls')),
    path('api/auth/',include('authentication.urls')),
    path('api/all-option/content/',content_view.GetAllOptionForContetAPIViewset.as_view()),
    path('api/password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
