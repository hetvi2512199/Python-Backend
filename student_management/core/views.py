from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView,View

from core import models as core_models
from core import serializers as core_serializer
# Create your views here.




class IndexView(View):
    def get(self, request):
        return render(request,'core/collages.html')

class IndexUpdateView(View):
    def get(self,request):
        return render(request,'core/collages_update.html')

#create
class CollageAPIView(APIView):
    def post(self , request ):
        req_data = request.data

        serializer_instance = core_serializer.CollageSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status=400, data = {"message":"data not found"})

        collage_create_instance = core_models.Collages.objects.create(

            collage_name = serializer_instance.validated_data.get('collage_name'),
            code = serializer_instance.validated_data.get("code"),
            collages_type = serializer_instance.validated_data.get('collages_type'),
            city = serializer_instance.validated_data.get("city")
        )
        return Response(status = 200 ,data = {"data":collage_create_instance.collage_get_details()})



#delete
class CollageDeleteAPIView(APIView):
    def post(self,request , id):
        collage_instance = core_models.Collages.objects.filter(id = id).last()
        if not collage_instance:
            return Response(status=400, data = {"message":"collage not exist"})

        collage_instance.delete()
        return Response(status = 200 ,data = {"message":"Collage successfully removed"})
   
#update
class UpdateCollageAPIView(APIView):
    def post(self ,request ,id ):
        req_data = request.data
        req_data.update({"collage_id":id})

        serializer_instance = core_serializer.UpdateCollageSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status=400, data = {"message":"school not exits"})

        collage_instance = serializer_instance.validated_data.get("collage_id")

        collage_name = serializer_instance.validated_data.get("collage_name")
        code = serializer_instance.validated_data.get("code")
        collages_type = serializer_instance.validated_data.get("collages_type")
        city = serializer_instance.validated_data.get("city")

        collage_instance.collage_name = collage_name
        collage_instance.code = code
        collage_instance.collages_type = collages_type
        collage_instance.city = city

        collage_instance.save()
        return Response(status = 200 ,data = {"data":collage_instance.collage_get_details()})


