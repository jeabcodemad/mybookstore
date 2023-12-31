# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from mybookstore.books.serializers import BookSerializer
# from .models import Book

# # Create your views here.
# @api_view(['GET'])
# def getAllBooks(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer