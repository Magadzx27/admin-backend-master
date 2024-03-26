from django.shortcuts import render
from .serializers import ProductsSerializer
from .models import Products
from rest_framework import permissions, status
from django.core import serializers

from rest_framework.response import Response
from rest_framework.views import APIView
from categories.models import Category
from .permissions import IsStaff
from categories.serializers import CategoriesSerializer
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Case, F, When
from django.db.models.expressions import Value


class ProductsAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        filter_dict = {}
        if request.user.is_staff:
            filter_dict['deleted'] = False
        else:
            filter_dict['active'] = True
            filter_dict['deleted'] = False
        if request.query_params.get('category_id', None):
            filter_dict['category_id'] = request.query_params.get(
                'category_id')
        if request.query_params.get('featured', None):
            filter_dict['featured'] = request.query_params.get('featured')
        if request.query_params.get('preorder', None):
            filter_dict['preorder'] = request.query_params.get('preorder')
        if request.query_params.get('search', None):
            filter_dict['name__icontains'] = request.query_params.get('search')
        if request.query_params.get('latest', None):
            queryset = Products.objects.all().filter(
                **filter_dict).order_by('created_date')[:int(request.query_params.get('latest', 10))]
        else:
            sort = request.query_params.get('sort', None)
            if sort == "1":
                queryset = Products.objects.all().filter(**filter_dict).order_by('-price')
            elif sort == "2":
                queryset = Products.objects.all().filter(**filter_dict).order_by('price')
            else:
                queryset = Products.objects.all().filter(**filter_dict)
            page_number = self.request.query_params.get('page_number', None)

            if page_number:
                paginator = Paginator(queryset, 20)
                try:
                    queryset = paginator.page(page_number)
                except (EmptyPage, InvalidPage):
                    queryset = Products.objects.none()

        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsDetailAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, **filter_dict):
        try:
            return Products.objects.get(**filter_dict)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        if request.user.is_staff:
            product = self.get_object(id=id, deleted=False)
        else:
            product = self.get_object(id=id, active=True, deleted=False)
        if isinstance(product, Products):
            serializer = ProductsSerializer(product)
            cat_serializer = CategoriesSerializer(product.category_id)
            return Response({'product': serializer.data, 'category': cat_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        product = self.get_object(id=id)
        if isinstance(product, Products):
            serializer = ProductsSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        product = self.get_object(id=id)
        if isinstance(product, Products):
            serializer = ProductsSerializer(
                product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsTest(APIView):
    permission_classes = [IsStaff]

    def get_object(self, **filter_dict):
        try:
            return Products.objects.get(**filter_dict)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        if request.user.is_staff:
            product = self.get_object(id=id, deleted=False)
        else:
            product = self.get_object(id=id, active=True, deleted=False)
        if isinstance(product, Products):
            serializer = ProductsSerializer(product)
            cat_serializer = CategoriesSerializer(product.category_id)
            return Response({'product': serializer.data, 'cat': cat_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
