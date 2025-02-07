from rest_framework import generics
from .serializers import UserRegistrationSerializer

class UserRegistrationViews(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self,request,*args,**kwargs):
        return self.creat(request,*args,**kwargs)