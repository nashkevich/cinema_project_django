from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

class UserRegistrationViews(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    def get_permissions(self):
        return [AllowAny()]
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)