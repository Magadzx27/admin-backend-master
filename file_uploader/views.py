from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings

from .serializers import UploderSerializer
from .models import UploderModel
import os
class FileUploaderView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = UploderSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploaderDetailAPIView(APIView):
    parser_class = (FileUploadParser,)
    queryset = UploderModel.objects.all()
    lookup_field = "file"

    def delete(self, request, *args, **kwargs):
        queryset = self.queryset.filter(file=self.kwargs.get("file"))
        if queryset:
            for image in queryset:
                if os.path.isfile(os.path.join(settings.MEDIA_ROOT,str(image.file))):
                    os.remove(os.path.join(settings.MEDIA_ROOT,str(image.file)))
                image.delete()
            return Response(status=200)
        else:
            return Response(status=400)