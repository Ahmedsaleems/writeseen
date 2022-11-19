from rest_framework.viewsets import ModelViewSet
from userprofile.models import UserProfileWriter, UserProfileIndustry, IAM
from userprofile import serializers as userprofile_serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from user.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserProfileIndustryViewSet(ModelViewSet):
    queryset = UserProfileIndustry.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def get_serializer_class(self):
        if self.action == 'list':
            return userprofile_serializers.RetriveUserIndustrySerializer
        if self.action == 'retrieve':
            return userprofile_serializers.RetriveUserIndustrySerializer
        return userprofile_serializers.UserIndustrySerializer

class UserProfileWriterViewSet(ModelViewSet):
    queryset = UserProfileWriter.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set
    def get_serializer_class(self):
        if self.action == 'list':
            return userprofile_serializers.RetriveUserWriterSerializer
        if self.action == 'retrieve':
            return userprofile_serializers.RetriveUserWriterSerializer
        return userprofile_serializers.UserWriterSerializer

class UserBasicInformationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userprofile_serializers.RetriveUserSerializer
    
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        queryset = self.queryset.filter(username=self.request.user.username)
        return queryset
    
    def list(self, request):
        return Response({'status_code':status.HTTP_401_UNAUTHORIZED,'message':'Invalid method call.'})
    
    def create(self, request):
        return Response({'status_code':status.HTTP_401_UNAUTHORIZED,'message':'Invalid method call.'})
    
    def destroy(self, request, *args, **kwargs):
        return Response({'status_code':status.HTTP_401_UNAUTHORIZED,'message':'Invalid method call.'})

class WhoIamUserWriterViewSet(ModelViewSet):
    queryset = IAM.objects.all()
    serializer_class = userprofile_serializers.IAMSerializer
    # permission_classes = (IsAuthenticated,)