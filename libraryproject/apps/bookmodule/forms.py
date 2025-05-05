from django import forms
from .models import Book , Address , Student ,Student3, Address3 ,Gallery

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

#lab11
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class Student3Form(forms.ModelForm):
    class Meta:
        model = Student3
        fields = '__all__'
        widgets = {
            'addresses': forms.CheckboxSelectMultiple()
        }

class Address3Form(forms.ModelForm):
    class Meta:
        model = Address3
        fields = '__all__'
        

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
