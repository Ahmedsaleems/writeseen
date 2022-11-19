from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from user.serializers import UserSerializer
from user.models import User
# from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from . import serializers
# Create your views here.
class ObtainJWTView(TokenObtainPairView):
    serializer_class = serializers.CustomJWTSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        # User = get_user_model()
        user = User.objects.filter(email=request.data.get("username")).first() or User.objects.filter(username=request.data.get("username")).first()
        # user_role = UserRole.objects.get(user=user)
        user_role_serializer = UserSerializer(instance=user)
        
        if request.session.session_key == None:
            request.session.cycle_key()
        
        data = dict(
            token=serializer.validated_data,
            session_key=request.session.session_key,
            user_details=user_role_serializer.data
        )

        return Response({'status':status.HTTP_200_OK, 'data':data})


class BlacklistRefreshView(APIView):
    def post(self, request):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response({'status_code':status.HTTP_200_OK, "message":"Successfully Logout."})
