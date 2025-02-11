from rest_framework import generics,views
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer,UserGetSerializer

class UserRegistrationViews(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    def get_permissions(self):
        return [AllowAny()]
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

class GetUserView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        user = request.user
        serializer = UserGetSerializer(user)
        return Response({'message':"Get user data",'response':serializer.data},status=200)