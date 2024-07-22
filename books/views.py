from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm
    return render(request, 'books/book_new.html', {'form': form})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')

def book_delete_page(request, pk):
  book = get_object_or_404(Book, pk=pk)
  return render(request, 'books/book_delete_page.html', {'book': book})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        book = form.save(commit=False)
        book.save()
        return redirect('book_detail', pk=book.pk)

    return render(request, 'books/book_edit.html', {'book': book, 'form': form})
