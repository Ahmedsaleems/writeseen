from django.urls import path
from . import views

app_name= 'user'

urlpatterns = [
    # path('writer/', views.UserWriterAPIView.as_view(), name='user_writer_signup'),
    # path('industry/', views.UserIndustryAPIView.as_view(), name='user_industry_signup'),
    path('signup/', views.UserSignupAPIView.as_view(), name='user_signup'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
]