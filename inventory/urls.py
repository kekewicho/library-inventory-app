from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("authors/", views.authors_view, name="authors"),
    path("authors/create/", views.author_create, name="author_create"),
    path("authors/<int:id>/", views.author_detail, name="author_detail"),
    path("authors/<int:id>/update/", views.author_update, name="author_update"),
    path("authors/<int:id>/delete/", views.author_delete, name="author_delete"),

    path("books/", views.books_view, name="books"),
    path("books/create/", views.book_create, name="book_create"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("books/<int:pk>/update/", views.book_update, name="book_update"),
    path("books/<int:pk>/delete/", views.book_delete, name="book_delete"),
]