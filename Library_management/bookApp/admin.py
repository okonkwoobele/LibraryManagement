
from django.contrib import admin
from .models import Author, Book


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['email']
    list_per_page = 20


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'price']
    list_filter = ['genre', 'language']
    list_per_page = 20



