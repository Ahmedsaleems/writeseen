from rest_framework.viewsets import ModelViewSet
from user.models import User
# from user.serializers import UserWriterSerializer, UserIndustrySerializer
from content import models as con_models
from content import serializers as con_serializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import MultiPartParser, FormParser
from collections import namedtuple
Options = namedtuple('Options', ('type', 'genr','language','tags'))

class TagsViewSet(ModelViewSet):
    queryset = con_models.TagsMaster.objects.all()
    serializer_class = con_serializer.TagsSerializer
    # permission_classes = (IsAuthenticated,)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ContentMasterViewSet(ModelViewSet):
    queryset = con_models.ContentMaster.objects.all()
    serializer_class = con_serializer.ContentMasterSerializer
    # permission_classes = (IsAuthenticated,)

class GenrMasterViewSet(ModelViewSet):
    queryset = con_models.GenrMaster.objects.all()
    serializer_class = con_serializer.GenrMasterSerializer
    # permission_classes = (IsAuthenticated,)

class TypeMasterViewSet(ModelViewSet):
    queryset = con_models.TypeMaster.objects.all()
    serializer_class = con_serializer.TypeMasterSerializer
    # permission_classes = (IsAuthenticated,)

class LanguageMasterViewSet(ModelViewSet):
    queryset = con_models.LanguageMaster.objects.all()
    serializer_class = con_serializer.LanguageMasterSerializer
    # permission_classes = (IsAuthenticated,)

class AuthorMasterViewSet(ModelViewSet):
    queryset = con_models.AuthorMaster.objects.all()
    serializer_class = con_serializer.AuthorMasterSerializer
    # permission_classes = (IsAuthenticated,)

class GetAllOptionForContetAPIViewset(APIView):
    def get(self, request, format=None):
        options = Options(
            type=con_models.TypeMaster.objects.all(),
            genr=con_models.GenrMaster.objects.all(),
            language=con_models.LanguageMaster.objects.all(),
            tags=con_models.TagsMaster.objects.all()
        )
        serializer = con_serializer.ContentOptionsSerializer(options)
        return Response(serializer.data)

class ContentViewSet(ModelViewSet):
    queryset = con_models.Content.objects.all()
    pagination_class = LimitOffsetPagination
    #permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    
    def get_queryset(self):
        queryset = self.queryset
        #query_set = queryset.filter(user=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return con_serializer.RetriveContentSerializer
        if self.action == 'retrieve':
            return con_serializer.RetriveContentSerializer
        return con_serializer.ContentSerializer
    

