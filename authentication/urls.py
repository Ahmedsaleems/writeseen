from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

app_name= 'authentication'

urlpatterns = [
    path('token/', views.ObtainJWTView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/',TokenVerifyView.as_view(),name="token_verify"),
    # path('logout/',views.BlacklistRefreshView.as_view(),name="back_list_refresh_token"),
]