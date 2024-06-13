from django.urls import path
from .views import hello, hello_rest_api,home, HelloWorldView, HelloWorldClassView, home_templates, create_book, book_list, BookAuthorView


urlpatterns = [
    path('hello/', hello),
    path('api/hello/', hello_rest_api, name = 'hello_rest_api'),
    path('api/home/', home),
    path('hellocbv/', HelloWorldView.as_view()),
    path('api/hellocbv/', HelloWorldClassView.as_view()),
    path('home/', home_templates),
    path('createbook/', create_book),
    path('booklist/', book_list, name='book_list'),
    path('createauthor/', BookAuthorView.as_view()),
]
