from rest_framework import generics,views
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from .models import LikedMoviesUser
from .serializers import UserRegistrationSerializer,UserGetSerializer,BasketSerializer

class UserRegistrationViews(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    def get_permissions(self):
        return [AllowAny()]
    def post(self,request,*args,**kwargs):
        repsonse = super().post(request,*args,**kwargs)
        user = User.objects.get(username=repsonse.data['username'])
        serializer = UserGetSerializer(user)
        LikedMoviesUser.objects.create(user_id=serializer.data['id'],basket=[])
        return repsonse
        
    

class GetUserView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        user = request.user
        serializer = UserGetSerializer(user)
        return Response({'message':"Get user data",'response':serializer.data},status=200)
    
class BasketUserView(views.APIView):
    def get(self,request,*args,**kwargs):
        userId = request.GET.get('userId')
        basket = LikedMoviesUser.objects.get(user__id=userId)
        serializer = BasketSerializer(basket)
        return Response({'message':"Get basket for user!",'response':serializer.data},status=200)
    
    def put(self,request,*args,**kwargs):
        data = request.data
        user = request.user
        serializer_user = UserGetSerializer(user)
        basket_object = LikedMoviesUser.objects.get(user_id=serializer_user.data['id'])
        basket_object.basket = data.get('basket')
        basket_object.save()
        return Response({"message":"Success updated basket object!"},status=200)