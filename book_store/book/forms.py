from django import forms
from .models import Book


class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


# 2 ways to write forms
'''
class BookForm(forms.Form):
    name= forms.CharField(max_length=100)
    published_date= forms.CharField(max_length=100)
    price= forms.FloatField( )
    category= forms.CharField(max_length=100)'''
