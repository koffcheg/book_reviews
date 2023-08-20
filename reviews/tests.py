from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import Book

# Model Tests
class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(title='Test Book', 
                            author='Test Author', 
                            publisher='Test Publisher',
                            release_date='2028-08-01',
                            amount=0)

    def test_book_creation(self):
        book = Book.objects.get(title='Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.publisher, 'Test Publisher')
        self.assertEqual(book.release_date, date(2028, 8, 1))
        self.assertEqual(book.amount, 0)  

# View Tests
class BookListViewTest(TestCase):
    def setUp(self):
        Book.objects.create(title='Test Book', 
                            author='Test Author', 
                            publisher='Test Publisher',
                            release_date='2028-08-01',
                            amount=0)

    def test_view_url_exists(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/book_list.html')
