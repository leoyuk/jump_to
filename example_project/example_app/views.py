from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Author, Book
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!")

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message' : 'Hello, REST API!'}
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
    first_book = Book.objects.first()

    #객체 업데이트
    book.title = "New Book Title"
    book.save()

    #객체 삭제
    book.delete()

    return render(request, "home.html")


