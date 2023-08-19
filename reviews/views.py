from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, ReviewForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a view displaying all books
    else:
        form = BookForm()
    return render(request, 'reviews/add_book.html', {'form': form})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')  # Redirect to a view displaying all reviews
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'reviews/book_list.html', {"books" : books})