from rest_framework.serializers import ModelSerializer
from content import models
from rest_framework import serializers
from user import serializers as user_serializer


class TagsSerializer(ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('created_at','updated_at')
        model = models.TagsMaster

class ContentMasterSerializer(ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('created_at','updated_at')
        model = models.ContentMaster

class AuthorMasterSerializer(ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('created_at','updated_at')
        model = models.AuthorMaster

class GenrMasterSerializer(ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('created_at','updated_at')
        model = models.GenrMaster

class TypeMasterSerializer(ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('created_at','updated_at')
        model = models.TypeMaster

class LanguageMasterSerializer(ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('created_at','updated_at')
        model = models.LanguageMaster

class ContentOptionsSerializer(ModelSerializer):
    type=TypeMasterSerializer(many=True, read_only=True)
    genr=GenrMasterSerializer(many=True, read_only=True)
    language=LanguageMasterSerializer(many=True, read_only=True)
    tags=TagsSerializer(many=True, read_only=True)
    
    class Meta:
        model=models.LanguageMaster
        fields = ('type','genr','language','tags')
    

class ContentSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Content


class RetriveContentSerializer(ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        fields = '__all__'
        model = models.Content
        depth = 1

    def get_user(self,object):
        return user_serializer.UserSerializer(object.user).data