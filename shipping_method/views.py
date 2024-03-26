from django.shortcuts import render
from .serializers import Shipping_methodSerializer
from .models import Shipping_method
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsStaff


class Shipping_methodAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        shippings = Shipping_method.objects.all().filter(deleted=False)
        serializer = Shipping_methodSerializer(shippings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Shipping_methodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Shipping_methodDetailAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, id):
        try: 
            return Shipping_method.objects.get(id=id, deleted=False)
        except Shipping_method.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        shippings = self.get_object(id)
        if isinstance(shippings, Shipping_method):
            serializer = Shipping_methodSerializer(shippings)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        shippings = self.get_object(id)
        if isinstance(shippings, Shipping_method):
            serializer = Shipping_methodSerializer(shippings, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        shippings = self.get_object(id)
        if isinstance(shippings, Shipping_method):
            serializer = Shipping_methodSerializer(
                shippings,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)