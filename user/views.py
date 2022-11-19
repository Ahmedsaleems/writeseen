from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import User
from user.serializers import UserSignupSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserWriterSerializer
    # permission_classes = (IsAuthenticated,)

class UserSignupAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [permission() for permission in self.permission_classes]
    
    def list(self, request):
        return Response({'status_code':status.HTTP_401_UNAUTHORIZED,'message':'Invalid method call.'})

# class UserWriterAPIView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserWriterSerializer
#     permission_classes = (IsAuthenticated,)
    
#     def get_permissions(self):
#         if self.request.method == 'POST':
#             return [AllowAny()]
#         return [permission() for permission in self.permission_classes]
    
#     def list(self, request):
#         return Response({'status_code':status.HTTP_401_UNAUTHORIZED,'message':'Invalid method call.'})


# class UserIndustryAPIView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserIndustrySerializer
#     permission_classes = (IsAuthenticated,)
    
#     def get_permissions(self):
#         if self.request.method == 'POST':
#             return [AllowAny()]
#         return [permission() for permission in self.permission_classes]
    
#     def list(self, request):
#         return Response({'status_code':status.HTTP_401_UNAUTHORIZED,'message':'Invalid method call.'})

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_403_FORBIDDEN)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            token = dict(
                    refresh=str(RefreshToken.for_user(self.object)),
                    access=str(RefreshToken.for_user(self.object).access_token)
                )
            if request.session.session_key == None:
                request.session.cycle_key()
            data = dict(
                token=token,
                session_key=request.session.session_key,
            )
            
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': data
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)