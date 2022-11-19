from rest_framework.serializers import ModelSerializer
from userprofile.models import UserProfileIndustry, UserProfileWriter, IAM
from user.models import User
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer

class RetriveUserSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name','email')
        model = User

class UserIndustrySerializer(ModelSerializer):
    class Meta:
        fields = ('user','profile_pic','phone_number','organization_name','industry','profession','company_email','company_phone_number','country','address','shelf','write_chat')
        model = UserProfileIndustry

class UserWriterSerializer(ModelSerializer):
    class Meta:
        fields = ('user','profile_pic','phone_number','about_me','iam','country','address','shelf','write_chat')
        model = UserProfileWriter


class RetriveUserIndustrySerializer(ModelSerializer):
    user= UserSerializer()
    
    class Meta:
        fields = ('user','profile_pic','phone_number','organization_name','industry','profession','company_email','company_phone_number','country','address','shelf','write_chat')
        model = UserProfileIndustry
        depth=1


class RetriveUserWriterSerializer(ModelSerializer):
    user= UserSerializer()
   
    class Meta:
        fields = ('user','profile_pic','phone_number','about_me','iam','country','address','shelf','write_chat')
        model = UserProfileWriter
        depth=1

class IAMSerializer(ModelSerializer):
    class Meta:
        fields = ('id','name',)
        model = IAM