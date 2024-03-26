from django.shortcuts import render
from .serializers import ReviewSerializer, ReadReviewsSerializer
from .models import Review
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsStaff

# Create your views here.


class ReviewAPIView(APIView):
    permission_classes = [IsStaff]

    def get(self, request):
        item_id = request.query_params.get('id')
        print(item_id)
        if not item_id:
            return Response({"error": "item_id is required!"}, status=status.HTTP_400_BAD_REQUEST)
        reviews = Review.objects.all().filter(item_id=item_id, deleted=False)
        serializer = ReadReviewsSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        serializer.initial_data['user_id'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailAPIView(APIView):
    permission_classes = [IsStaff]

    def get_object(self, id, deleted=None):
        try:
            return Review.objects.get(id=id, deleted=deleted)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        category = self.get_object(id, deleted=False)
        if isinstance(category, Review):
            serializer = ReviewSerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        category = self.get_object(id, deleted=False)
        if isinstance(category, Review):
            serializer = ReviewSerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        category = self.get_object(id, deleted=False)
        if isinstance(category, Review):
            serializer = ReviewSerializer(
                category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def delete(self, request, id):
    #     tag = self.get_object(id)
    #     tag.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
