from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, null=True)
    release_date = models.DateField(default='2000-07-01')
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review for {self.book.title}"
