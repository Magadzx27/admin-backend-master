from .serializers import ImagesliderSerializer
from .models import Imageslider
from rest_framework import permissions
from .permissions import IsStaff
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ImagesliderAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        imageslider = Imageslider.objects.all()
        serializer = ImagesliderSerializer(imageslider, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImagesliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImagesliderValueAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, id):
        try:
            return Imageslider.objects.get(id=id)
        except Imageslider.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        imageslider = self.get_object(id)
        if isinstance(imageslider, Imageslider):
            serializer = ImagesliderSerializer(imageslider)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        imageslider = self.get_object(id)
        if isinstance(imageslider, Imageslider):
            serializer = ImagesliderSerializer(imageslider, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        imageslider = self.get_object(id)
        if isinstance(imageslider, Imageslider):
            serializer = ImagesliderSerializer(
                imageslider, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, id):
        imageslider = self.get_object(id)
        print(imageslider)
        if isinstance(imageslider, Imageslider):
            imageslider.delete()
            Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
