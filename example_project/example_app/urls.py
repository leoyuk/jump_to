from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, hello, hello_rest_api,home, HelloWorldView, HelloWorldClassView, home_templates, create_book, book_list, BookAuthorView, create_book_byserializer, print_book

# booklist = BookViewSet.as_view({
#     'get' : 'list',
#     'post' : 'create'
# })

# bookdetail = BookViewSet.as_view({
#     'get' : 'retrieve',
#     'put' : 'update',
#     'delete' : 'destroy'
# })

router = routers.DefaultRouter()
router.register('books', BookViewSet)

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
    path('api/createbook/', create_book_byserializer, name='create_book_byserializer'),
    path('api/retrievebook/', print_book,),
    path('api/', include(router.urls)),
    # path('api/book/', booklist, name='book-list'),
    # path('api/book/<int:pk>', bookdetail, name="book-detail"),
]
