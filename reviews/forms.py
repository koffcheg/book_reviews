from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'release_date', 'amount']  # Add other fields if needed

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'review_text', 'rating']  # Add other fields if needed
