from django.contrib import admin
from .models import Book, Author
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'price']
    search_fields = ['title', 'author__name']
    list_filter = ['author', 'published_date']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass