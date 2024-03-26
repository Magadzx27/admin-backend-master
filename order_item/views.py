from .serializers import Orders_itemSerializer, ReadOrderItemsSerializer
from .models import Orders_item
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsStaff

class Orders_itemAPIView(APIView):
    permission_classes = [IsStaff]
    
    def get(self, request):
        order_id = request.query_params.get('order_id')
        if not order_id:
            return Response({"error":"order_id is required!"}, status=status.HTTP_400_BAD_REQUEST)
        if request.user.is_staff:
            orders_item = Orders_item.objects.all().filter(order_id=order_id)
        else:
            orders_item = Orders_item.objects.all().filter(user_id=request.user,order_id=order_id)
        serializer = ReadOrderItemsSerializer(orders_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Orders_itemSerializer(data=request.data)
        serializer.initial_data['user_id'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Orders_itemValueAPIView(APIView):
    permission_classes = [IsStaff]
    
    def get_object(self, id):
        try: 
            return Orders_item.objects.get(id=id)
        except Orders_item.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        orders_item = self.get_object(id)
        if isinstance(orders_item, Orders_item):
            self.check_object_permissions(request, orders_item)
            serializer = ReadOrderItemsSerializer(orders_item)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    # def put(self, request, id):
    #     orders_item = self.get_object(id)
    #     if isinstance(orders_item, Orders_item):
    #         self.check_object_permissions(request, orders_item)
    #         serializer = Orders_itemSerializer(orders_item, data=request.data)
    #         serializer.initial_data['user_id'] = request.user.id
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def patch(self, request, id):
    #     orders_item = self.get_object(id)
    #     if isinstance(orders_item, Orders_item):
    #         self.check_object_permissions(request, orders_item)
    #         serializer = Orders_itemSerializer(
    #             orders_item, data=request.data, partial=True)
    #         serializer.initial_data['user_id'] = request.user.id
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def delete(self, request, id):
    #     orders_item = self.get_object(id)
    #     if isinstance(orders_item, Orders_item):
    #         self.check_object_permissions(request, orders_item)
    #         orders_item.delete()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_204_NO_CONTENT)
