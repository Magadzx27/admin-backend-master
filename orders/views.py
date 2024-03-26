from .serializers import OrdersSerializer
from .models import Orders
from .permissions import IsStaff
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.template.loader import render_to_string
from authentication.utils import Util
from authentication.serializers import RegisterSerializer
from authentication.models import User
from shipping_method.serializers import Shipping_methodSerializer
from payment_method.serializers import Payment_methodSerializer
from authentication.serializers import UserSerializer

class OrdersAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        filter_dict = {}
        execlude_dict = {}
        if request.query_params.get('store_status', None):
            filter_dict['store_status'] = request.query_params.get('store_status')
        if request.query_params.get('user_status', None):
            filter_dict['user_status'] = request.query_params.get('user_status')
        if request.user.is_staff:
            if filter_dict.get('store_status', None):
                order = Orders.objects.all().filter(**filter_dict)
            else:
                order = Orders.objects.all().filter(**filter_dict).exclude(store_status='Archive')
        else:
            if filter_dict.get('user_status', None):
                order = Orders.objects.all().filter(user_id=request.user, **filter_dict)
            else:
                order = Orders.objects.all().filter(user_id=request.user, **filter_dict).exclude(user_status='Archive')
        serializer = OrdersSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        serializer.initial_data['user_id'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersValueAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, id):
        try:
            return Orders.objects.get(id=id)
        except Orders.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        order = self.get_object(id)
        if isinstance(order, Orders):
            self.check_object_permissions(request, order)
            serializer = OrdersSerializer(order)
            shipping_method_serializer = Shipping_methodSerializer(order.shipping_id)
            payment_method_serializer = Payment_methodSerializer(order.payment_id)
            user_serializer = UserSerializer(order.user_id)
            return Response({'order': serializer.data, 'shipping_method':shipping_method_serializer.data,'payment_method':payment_method_serializer.data, 'user': user_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        order = self.get_object(id)
        if isinstance(order, Orders):
            self.check_object_permissions(request, order)
            serializer = OrdersSerializer(order, data=request.data)
            serializer.initial_data['user_id'] = request.user.id
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        order = self.get_object(id)
        if isinstance(order, Orders):
            self.check_object_permissions(request, order)
            serializer = OrdersSerializer(
                order, data=request.data, partial=True)
            serializer.initial_data['user_id'] = request.user.id
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def delete(self, request, id):
    #     order = self.get_object(id)
    #     if isinstance(order, Orders):
    #         self.check_object_permissions(request, order)
    #         order.delete()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_204_NO_CONTENT)


class CheckoutAPIView(APIView):
    permission_classes = [IsStaff]

    def post(self, request):
        user = request.user
        html_content = render_to_string('confirm_order.html', {
                                        'site': user, 'username': user.username,'name': user.name, 'email': user.email})
        data = {'email_body': html_content, 'to_email': user.email,
                'email_subject': 'Order confirmation email', 'html_message': html_content}
        Util.send_email(data)
        return Response(status=status.HTTP_200_OK)
