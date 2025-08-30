# inventory/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# Vistas para el modelo Autor
def authors_view(r):
    authors = Autor.objects.annotate(count_libros = Count('libro'))
    form = AutorForm()
    context = {
        "authors": authors,
        "form": form
    }
    return render(r, "inventory/authors.html", context)

def author_detail(r, id: int):
    autor = get_object_or_404(Autor, id=id)
    books = Libro.objects.filter(autor = id)
    context = {
        "author": autor,
        "books": books
    }
    return render(r, "inventory/author_detail.html", context)

def author_create(r):
    if r.method == "POST":
        form = AutorForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect("authors")
    else:
        form = AutorForm()
    
    context = {
        "form": form
    }
    return render(r, "inventory/author_form.html", context)

def author_update(r, id: int):
    autor = get_object_or_404(Autor, id=id)
    form = AutorForm(r.POST, instance=autor)
    if form.is_valid():
        form.save()
        return redirect("author_detail", id=autor.id)
    

def author_delete(r, id: int):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return redirect("authors")

def books_view(r):
    books = Libro.objects.all()
    form = LibroForm()
    context = {
        "books": books,
        "form": form
    }
    return render(r, "inventory/books.html", context)

def book_detail(r, pk: int):
    libro = get_object_or_404(Libro, pk=pk)
    context = {
        "book": libro
    }
    return render(r, "inventory/book_detail.html", context)

def book_create(r):
    form = LibroForm(r.POST)
    if form.is_valid():

        form.instance.last_update = timezone.now()

        form.save()
        return redirect("books")
    

def book_update(r, pk: int):
    libro = get_object_or_404(Libro, pk=pk)
    
    form = LibroForm(r.POST, instance=libro)
    if form.is_valid():
        form.instance.last_update = timezone.now()
        form.save()
        return redirect("book_detail", pk=libro.pk)

def book_delete(r, pk: int):
    libro = get_object_or_404(Libro, pk=pk)
    libro.delete()
    return redirect("books")
    

def index(r):
    return redirect("books")