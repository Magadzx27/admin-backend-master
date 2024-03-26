from django.shortcuts import render
from .serializers import Payment_methodSerializer
from .models import Payment_method
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsStaff

class Payment_methodAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        method = Payment_method.objects.all().filter(deleted=False)
        serializer = Payment_methodSerializer(method, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Payment_methodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Payment_methodDetailAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, id):
        try: 
            return Payment_method.objects.get(id=id, deleted=False)
        except Payment_method.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        method = self.get_object(id)
        if isinstance(method, Payment_method):
            serializer = Payment_methodSerializer(method)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        method = self.get_object(id)
        if isinstance(method, Payment_method):
            serializer = Payment_methodSerializer(method, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        method = self.get_object(id)
        if isinstance(method, Payment_method):
            serializer = Payment_methodSerializer(
                method,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
