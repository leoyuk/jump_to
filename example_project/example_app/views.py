from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import HttpResponse
from django.views import View

from .serializers import BookSerializer

from .models import Author, Book
from django.shortcuts import render, redirect

from django import forms
from .forms import ContactFrom, BookForm, BookAuthorForm

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


def home_templates(request):
    data = {
        'name' : 'John Doe',
        'age' : 25,
        'country' : 'USA',
    }
    return render(request, 'example_app/home.html', context=data)


class UserRegister(View):
    def post(self, request):
        form = ContactFrom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']



def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')

    else : #method get
        form = BookForm()
    return render(request, 'example_app/create_book.html', {'form':form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'example_app/book_list.html', {'books':books})

class BookAuthorView(View):

    def get(self, request):
        form = BookAuthorForm()
        return render(request, 'example_app/create_author.html', {'form':form})

    def post(self, request):
        form = BookAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')

        else :
            BookAuthorView.get(request)



@api_view(['POST'])
@permission_classes([AllowAny])
def create_book_byserializer(request):
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([AllowAny])
def print_book(request):
    book = Book.objects.get(id = 1)
    serializer = BookSerializer(book)
    return Response(serializer.data)



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
