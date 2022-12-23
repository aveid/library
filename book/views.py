from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serializers import BookSerializers, BookUpdateSerializer


class BookAPIView(APIView):

    def get(self, request, format=None):
        books = Book.objects.all()
        serializers = BookSerializers(books, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BookSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailUpdateDeleteAPIView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializers(book)
            return Response(serializer.data)
        except Book.DoesNotExist as err:
            raise ValidationError(
                {"error": err}
            )

    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookUpdateSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)