"""
URL configuration for example_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from example_app.views import hello, hello_rest_api,home, HelloWorldView, HelloWorldClassView, home_templates, create_book, book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('api/hello/', hello_rest_api, name = 'hello_rest_api'),
    path('api/home/', home),
    path('hellocbv/', HelloWorldView.as_view()),
    path('api/hellocbv/', HelloWorldClassView.as_view()),
    path('home/', home_templates),
    path('createbook/', create_book),
    path('booklist/', book_list)

]
