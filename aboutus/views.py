from .serializers import AboutusSerializer
from .models import Aboutus
from rest_framework import permissions
from .permissions import IsStaff
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class AboutusAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        abouts = Aboutus.objects.all()
        serializer = AboutusSerializer(abouts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AboutusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutusValueAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, key):
        try:
            return Aboutus.objects.get(key=key)
        except Aboutus.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, key):
        abouts = self.get_object(key)
        if isinstance(abouts, Aboutus):
            serializer = AboutusSerializer(abouts)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, key):
        aboutus = self.get_object(key)
        if isinstance(aboutus, Aboutus):
            serializer = AboutusSerializer(aboutus, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, key):
        aboutus = self.get_object(key)
        if isinstance(aboutus, Aboutus):
            serializer = AboutusSerializer(
                aboutus, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = AboutusSerializer(data={'key': key, 'value': request.data.get("value")})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, key):
        abouts = self.get_object(key)
        if isinstance(abouts, Aboutus):
            abouts.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
