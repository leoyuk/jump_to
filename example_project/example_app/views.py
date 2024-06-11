from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views import View

from .models import Author, Book
from django.shortcuts import render

# Function Based View
def hello(request):
    return HttpResponse("Hello, world!")

# Class Based View
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")

# Fuction Based View with Django REST Framework
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message' : 'Hello, REST API!'}
    return Response(data)


# Class Based View with Django REST Framework
@permission_classes([AllowAny])
class HelloWorldClassView(APIView):
    def get(self, request):
        data = {'message' : 'Hello, APIView!'}
        return Response(data)

def home(request):
    # 객체 생성 및 데이터 베이스에 저장
    author = Author(name = "John Doe", age=30)
    author.save()

    book = Book(title="First Book", author=author)
    book.save()

    #데이터 베이스에서 객체 검색

    books = Book.objects.all() # 모든 책 검색
    book = Book.objects.get(title = 'First Book') # 특정 책 검색
    first_book = Book.objects.first() # 첫번째 책 검색
    last_book = Book.objects.last() # 마지막 책 검색

    print(book.title)
    print(first_book.author.name)
    print(last_book.author.name)

    #객체 업데이트
    book.title = "New Book Title"
    book.save()

    print(book.title)

    #객체 삭제
    book.delete()

    book_data = {"first_book" : first_book.author.name}

    return HttpResponse(book_data["first_book"])


