from .serializers import CategoriesSerializer
from .models import Category
from .permissions import IsStaff
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CategoriesAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        if request.user.is_staff:
            categories = Category.objects.all().filter(
                parent=request.query_params.get('parent', None), deleted=False)
        else:
            categories = Category.objects.all().filter(
                parent=request.query_params.get('parent', None), active=True, deleted=False)
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesDetailAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, **filter_dict):
        try:
            return Category.objects.get(**filter_dict)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        if request.user.is_staff:
            category = self.get_object(id=id, deleted=False)
        else:
            category = self.get_object(id=id, active=True, deleted=False)
        if isinstance(category, Category):
            serializer = CategoriesSerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        category = self.get_object(id=id)
        if isinstance(category, Category):
            serializer = CategoriesSerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        category = self.get_object(id=id)
        if isinstance(category, Category):
            serializer = CategoriesSerializer(
                category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
