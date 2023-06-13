from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from app.models import *
from app.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



@permission_classes([IsAuthenticated])
class ProductCrud(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PJD=products(PQS,many=True)
        return Response(PJD.data)
    def post(self,request,id):
        PMSD=products(data=request.data)
        if PMSD.is_valid():
            spo=PMSD.save()
            return Response({"message":"product is created"})
        
        return Response({"faield":"product is not created"})
      
    def put(self,request,id):
        id=request.data['id']
        
        po=Product.objects.get(id=id)
       
        UPO=products(po,data=request.data)
        if UPO.is_valid():
            spo=UPO.save()
            return Response({"message":"product is updated"})
        
        return Response({"faield":"product is not updated"})
    def patch(self,request,id):
        
        id=request.data['id']
        
        po=Product.objects.get(id=id)
       
        UPO=products(po,data=request.data,partial=True)
        if UPO.is_valid():
            spo=UPO.save()
            return Response({"message":"product is updated"})
        
        return Response({"faield":"product is not updated"})

       
       
        
    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response ({'success':'product is delected'})
        


      

    
    

