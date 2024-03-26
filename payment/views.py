from .serializers import PaymentSerializer
from .models import Payment
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsStaff


class PaymentAPIView(APIView):
    permission_classes = [IsStaff]
    
    def get(self, request):
        order_id = request.query_params.get('order_id')
        if not order_id:
            return Response({"error":"order_id is required!"}, status=status.HTTP_400_BAD_REQUEST)
        if request.user.is_staff:
            payment = Payment.objects.all().filter(order_id=order_id)
        else:
            payment = Payment.objects.all().filter(user_id=request.user, order_id=order_id)
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.initial_data['user_id'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentValueAPIView(APIView):
    permission_classes = [IsStaff]
    
    def get_object(self, id):
        try: 
            return Payment.objects.get(id=id)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        payment = self.get_object(id)
        if isinstance(payment, Payment):
            self.check_object_permissions(request, payment)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    # def put(self, request, id):
    #     payment = self.get_object(id)
    #     if isinstance(payment, Payment):
    #         self.check_object_permissions(request, payment)
    #         serializer = PaymentSerializer(payment, data=request.data)
    #         serializer.initial_data['user_id'] = request.user.id
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def patch(self, request, id):
    #     payment = self.get_object(id)
    #     if isinstance(payment, Payment):
    #         self.check_object_permissions(request, payment)
    #         serializer = PaymentSerializer(
    #             payment, data=request.data, partial=True)
    #         serializer.initial_data['user_id'] = request.user.id
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def delete(self, request, id):
    #     payment = self.get_object(id)
    #     if isinstance(payment, Payment):
    #         self.check_object_permissions(request, payment)
    #         payment.delete()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_204_NO_CONTENT)
