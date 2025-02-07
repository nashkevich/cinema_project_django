from django.shortcuts import render
from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import MovieSerializer
from .models import Movie
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Create your views here.
class MovieApiView(views.APIView):
    # Api for Moives
    serializer_class = MovieSerializer

    def get_serializer_context(self):
        return {
            "request" : self.request,
            "format" : self.format_kwarg,
            "view" : self
        }

    def get_serializer(self,*args,**kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args,**kwargs)
    
    def post(self,request):
        try:
            data = JSONParser().parse(request)
            serializer = MovieSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result":"error","message":"Json Decoder Error"},status=400)
        
    def get(self,request,*args,**kwargs):
        try:
            movie_id = kwargs.get('id','')
            page = request.GET.get('page')
            limit = request.GET.get('limit')
            isCount = bool(request.GET.get('isCount'))
            if movie_id:
                movies = Movie.objects.get(id=movie_id)
                try:
                    serializer = MovieSerializer(movies)
                    return Response({"response":serializer.data,"message":"Movie found"},status=200)
                except Movie.DoesNotExist:
                    return Response({"message":"Movie not found"},status=404)
            elif page and limit:
                page = int(page)
                limit = int(limit)
                index_from = (page*limit) - limit
                index_to = (page*limit)
                try:
                    movies = Movie.objects.all()[index_from:index_to]
                    serializer = MovieSerializer(movies,many=True)
                    return Response({"message":f"Return movies from {index_from} to {index_to}","response":serializer.data},status=200)
                except Exception as e:
                    return Response({"message":e},status=500)
            elif isCount:
                movies = Movie.objects.all()
                serializer = MovieSerializer(movies,many=True)
                return Response({"message": "Return number of all movies","response":len(serializer.data)},status=200)
            else:
                movies = Movie.objects.all()
                serializer = MovieSerializer(movies,many=True)
                return Response({"response":serializer.data,"message":"All movies"},status=200)
        except Exception as e:
            return Response({"message":"failed","error":e},status=500)
        
    def delete(self,request):
        movies = Movie.objects.all().delete()
        return Response({"message":"All movies were deleted"},status=200)
