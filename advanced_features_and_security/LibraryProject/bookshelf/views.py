from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import permission_required

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # ... (book creation logic) ...

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    # ... (book editing logic) ...

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    # ... (book deletion logic) ...
