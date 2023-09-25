from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .serializer import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

##for creating user defined actions
# class UserViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset= User.objects.all()
#         serializer= UserSerializer(queryset, many= True, context={'request': request})
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk= None):
#         queryset= User.objects.all()
#         user= get_object_or_404(queryset, pk=pk)
#         serializer= UserSerializer(user, context={'request': request})
#         return Response(serializer.data)

class UserViewset(viewsets.ModelViewSet):
    serializer_class= UserSerializer
    queryset= User.objects.all()
    # permission_classes= [IsAdminUser]

    ##setting permissions if required
    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]