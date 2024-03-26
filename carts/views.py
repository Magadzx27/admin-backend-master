from django.shortcuts import render
from .serializers import CartsSerializer, ReadCartsSerializer
from .models import Carts
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsStaff

# Create your views here.


class CartsAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        if request.user.is_staff:
            cart = Carts.objects.all()
        else:
            cart = Carts.objects.all().filter(user_id=request.user)
        serializer = ReadCartsSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartsSerializer(data=request.data)
        serializer.initial_data['user_id'] = request.user.id
        filter_query = Carts.objects.filter(
            user_id=request.user.id, product_id=request.data.get('product_id'))
        item_exist = filter_query.first()
        if item_exist:
            item_exist.quantity = quantity = item_exist.quantity + \
                request.data.get('quantity', 1)
            item_exist.save(update_fields=['quantity'])
            return Response({"updated": True}, status=status.HTTP_200_OK)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartsDetailAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, id):
        try:
            return Carts.objects.get(id=id)
        except Carts.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        cart = self.get_object(id)
        if isinstance(cart, Carts):
            self.check_object_permissions(request, cart)
            serializer = ReadCartsSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        cart = self.get_object(id)
        if isinstance(cart, Carts):
            self.check_object_permissions(request, cart)
            serializer = CartsSerializer(cart, data=request.data)
            serializer.initial_data['user_id'] = request.user.id
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        cart = self.get_object(id)
        if isinstance(cart, Carts):
            self.check_object_permissions(request, cart)
            serializer = CartsSerializer(cart, data=request.data, partial=True)
            serializer.initial_data['user_id'] = request.user.id
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, id):
        cart = self.get_object(id)
        if isinstance(cart, Carts):
            self.check_object_permissions(request, cart)
            cart.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
