from django.db import models


class BaseBook(models.Model):
    name = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ImageBook(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Images of books'

    def __str__(self):
        return self.name


class Book(BaseBook):
    CATEGORY_CHOICES = [('MT', 'math'),
                        ('SC', 'science'),
                        ('HS', 'history'),
                        ]
    price = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, db_index=True, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image_book = models.ManyToManyField(ImageBook, related_name='books', null=True, blank=True)
    author = models.ForeignKey('user.Author', related_name='books',related_query_name="query_books", on_delete=models.CASCADE, null=True, blank=True,
                               default=None)

    class Meta:
        verbose_name = 'Book'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + " " + self.name
