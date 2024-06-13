from dataclasses import fields
from django import forms
from example_app.models import Book, Author

#Form declare like model
class ContactFrom(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


#Model Based Form
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'