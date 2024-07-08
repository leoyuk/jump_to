from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, hello, hello_rest_api,home, HelloWorldView, HelloWorldClassView, home_templates, create_book, book_list, BookAuthorView, create_book_byserializer, print_book
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "My Project API",
        default_version="V1",
        description="API docs for my project",
        terms_of_service="https://www.exampleproject.com/terms/",
        contact=openapi.Contact(email="contact@example.com"), license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    # path('docs/', include('rest_framework_docs.urls')),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
