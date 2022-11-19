from rest_framework.serializers import ModelSerializer
from user.models import User
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'is_writer', 'is_industry', 'created_at')
        model = User
        extra_kwargs = {'password': {'write_only': True}}

class UserSignupSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'is_writer', 'is_industry', 'profession', 'company_name')
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user

# class UserWriterSerializer(ModelSerializer):
#     class Meta:
#         fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'is_writer')
#         model = User
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create(**validated_data)
#         user.set_password(validated_data['password'])
#         user.is_staff = True
#         user.save()

#         return user

# class UserIndustrySerializer(ModelSerializer):
#     class Meta:
#         fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'is_industry', 'profession', 'company_name')
#         model = User
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create(**validated_data)
#         user.set_password(validated_data['password'])
#         user.is_staff = True
#         user.save()

#         return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
