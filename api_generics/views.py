from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

class UserList(generics.ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer
    # permission_classes= [IsAdminUser]

    def list(self, request):
        queryset= self.get_queryset()
        serializer= UserSerializer(queryset, many= True, context={'request': request})
        return Response(serializer.data)