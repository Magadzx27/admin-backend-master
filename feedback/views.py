from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.template.loader import render_to_string
from authentication.utils import Util
from aboutus.models import Aboutus
from aboutus.serializers import AboutusSerializer

class SendFeedAPIView(APIView):
    def post(self,request):
        try:
            to_email_obj = Aboutus.objects.get(key='contact_email')
            to_email_serializer = AboutusSerializer(to_email_obj)
            to_email = to_email_serializer.data.get("value")
            email=request.data['email']
            message=request.data['message']
            phone_number=request.data['phone']
            subject= request.data['subject']
            name= request.data['name']
            html_content = render_to_string('feedback.html', {'name': name , 'email':email,'message':message,'phone_number':phone_number})
            data={'email_body':html_content,'to_email':to_email,'email_subject':subject}
            Util.send_email(data)
            return Response(status=status.HTTP_200_OK)
        except Aboutus.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)        