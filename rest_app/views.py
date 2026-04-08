from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.


class ProductCRUDAPI(APIView):
   def post(self,request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Product Created Successfully','data':serializer.data},status=status.HTTP_201_CREATED)
            else:
                return Response({'message':'Not Created'})
              
        except Exception as e:
            return Response({"error":str(e)})
        
   def get(self,request,product_id=None):
       try:
           if product_id:
               product = Product.objects.get(id=product_id)
               serializer = ProductSerializer(data=request.data)
               if serializer.is_valid():
                   return Response({'message':'Product Get','data':serializer.data})
           else:
               product = Product.objects.all()
               serializer = ProductSerializer(product,many=True)
               return Response(serializer.data)
               
       except Exception as e:
           return Response({"error":str(e)})            
        
   def put(self,request,product_id):
       try:
           if product_id:
               product = Product.objects.get(id=product_id)
               serializer = ProductSerializer(product,data=request.data)
               if serializer.is_valid():
                   serializer.save()
                   return Response({'message':'Product Update','data':serializer.data}) 
               
       except Exception as e:
           return Response({'error':str(e)})   
       
   def patch(self,request,product_id):
       try:
           product = Product.objects.filter(id=product_id).first()
           if product_id:
               product = Product.objects.get(id=product_id)
               serializer = ProductSerializer(product,data=request.data,partial=True)
               if serializer.is_valid():
                   serializer.save()
                   return Response({'message':'Product Patch','data':serializer.data})   
               else:
                    return Response({'error': 'Product not found'},status=status.HTTP_404_NOT_FOUND)
                      
       except Exception as e:
           return Response({'error':str(e)})  
       
   def delete(self,request,product_id):
           try:
               if product_id:
                product = Product.objects.get(id=product_id)
               product.delete()
               return Response({'message':'Product Deleted'})
           
           except Exception as e:
               return Response({'error':str(e)})            
       
@api_view(['POST','GET'])    
def ProductCRUD(request,product_id=None):
       if request.method == 'POST':
           try:
               serializer = ProductSerializer(data=request.data)
               if serializer.is_valid():
                   serializer.save()
                   return Response({'message':'Product Created Successfully','data':serializer.data})      
               else:
                   return Response({'message':'Not Created'})
               
           except Exception as e:
               return Response({'error':str(e)})
           
       elif request.method == 'GET':
           try:
               if product_id:
                   product  = Product.objects.get(id=product_id)
                   serializer = ProductSerializer(product)
                   return Response(serializer.data)
               else:
                   products = Product.objects.all()
                   serializer = ProductSerializer(products,many=True)
                   return Response(serializer.data)
               
           except Exception as e:
               return Response({'error':str(e)})
                       
                       
class CRGeneric(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class UDGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CRUDViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer