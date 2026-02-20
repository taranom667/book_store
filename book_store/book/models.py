from django.db import models

from user.models import User


class BaseBook(models.Model):
    name = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Book(BaseBook):
    CATEGORY_CHOICES = [('MT', 'math'),
                        ('SC', 'science'),
                        ('HS', 'history'),
                        ]
    price = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, db_index=True)
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', related_query_name='book_query',
                             blank=True, null=True)

    class Meta:
        verbose_name = 'Book'

    def __str__(self):
        return self.name


class ImageBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images', related_query_name='image_query')
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Images of books'

    def __str__(self):
        return self.name
