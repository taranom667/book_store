from django.db import models

# Create your models here.
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
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,db_index=True )


    def __str__(self):
        return self.name


class DiffrentBook(BaseBook):
    pass



class ImageBook(models.Model):
    book= models.ForeignKey(Book,on_delete=models.CASCADE,related_name='images',related_query_name='image_query ')
    name = models.CharField(max_length=100)
