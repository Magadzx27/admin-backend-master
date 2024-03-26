from django.shortcuts import render
from .serializers import ShippingSerializer
from .models import Shipping
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsStaff


class ShippingsAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        order_id = request.query_params.get('order_id')
        if not order_id:
            return Response({"error":"order_id is required!"}, status=status.HTTP_400_BAD_REQUEST)
        shipping = Shipping.objects.all().filter(order_id=order_id)
        serializer = ShippingSerializer(shipping, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShippingSerializer(data=request.data)
        serializer.initial_data['user_id'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShippingsDetailAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, id):
        try: 
            return Shipping.objects.get(id=id)
        except Shipping.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        shipping = self.get_object(id)
        if isinstance(Shipping, shipping):
            self.check_object_permissions(request, shipping)
            serializer = ShippingSerializer(shipping)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def put(self, request, id):
    #     shipping = self.get_object(id)
    #     if isinstance(shipping, Shipping):
    #         self.check_object_permissions(request, shipping)
    #         serializer = ShippingSerializer(shipping, data=request.data)
    #         serializer.initial_data['user_id'] = request.user.id
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def patch(self, request, id):
    #     shipping = self.get_object(id)
    #     if isinstance(shipping, Shipping):
    #         self.check_object_permissions(request, shipping)
    #         serializer = ShippingSerializer(
    #             shipping, data=request.data, partial=True)
    #         serializer.initial_data['user_id'] = request.user.id
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def delete(self, request, id):
    #     shipping = self.get_object(id)
    #     if isinstance(shipping, Shipping):
    #         self.check_object_permissions(request, shipping)
    #         shipping.delete()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_204_NO_CONTENT)
