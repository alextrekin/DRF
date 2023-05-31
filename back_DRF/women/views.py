from django.forms import model_to_dict
from django.shortcuts import render
from .models import Category, Women
from .serializers import WomenSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

# Create your views here.

class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)
    
    @action(method=['get'],detail=False)
    def category(self, request):
        cats = Category.object.all()
        return Response({'cats':[c.name for c in cats]})        

# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     seralizer_class = WomenSerializer
    
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     seralizer_class = WomenSerializer  
    
# class WomenApiDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     seralizer_class = WomenSerializer  
# class WomanAPIView(APIView):
#     def get(self,request):
#         w = Women.objects.all()
#         return Response ({'posts':WomenSerializer(w,many=True,).data})
    
#     def post(self,request):
#         serializer = WomenSerializer(data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"post": serializer.data})
    
#     def put(self,request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             isinstance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error":"Object does not exist"})
        
#         serializer = WomenSerializer(data=request.data,instance=instance)
#         serializer.is_valid(raise_exception=TRUE)
#         serializer.save()
#         return Response({"post":serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#             pk = kwargs.get("pk", None)
#             if not pk:
#                 return Response({"error": "Method DELETE not allowed"})
            
#             try:
#                 record= Women.objects.get(pk=pk)
#                 record.delete()
#             except:
#                 return Response({"error": "Object does not exists"})

#             return Response({"post": "delete post " + str(pk)})