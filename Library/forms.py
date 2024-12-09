from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from account.models import User
from .models import *

class CreateBookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields=('title' , 'content' , 'created_at' , 'publisher' , 'the_author', 'educational_base' , 'category' , 'leason' , 'type' , 'users' , 'image')
        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':' نام کتاب' , 'style':'text-align: right!important;'}),
            'content':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':' توضیحات' , 'style':'text-align: right!important;'}),
            'created_at':forms.NumberInput(attrs={'class': 'form-control' , 'placeholder':'سال انتشار' , 'style':'text-align: right!important;'}),
            'publisher':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':' منتشر کننده' , 'style':'text-align: right!important;'}),
            'the_author':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':' مولفان' , 'style':'text-align: right!important;'}),
            'educational_base':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':' پایه تحصیلی' , 'style':'text-align: right!important;'}),
            # 'category':forms.ModelMultipleChoiceField(queryset=Category.objects.all() , widget=forms.CheckboxSelectMultiple),
            # 'leason':forms.ModelMultipleChoiceField(queryset=Leason.objects.all() , widget=forms.CheckboxSelectMultiple),
            # 'type':forms.ModelMultipleChoiceField(queryset=Type.objects.all() , widget=forms.CheckboxSelectMultiple),
            'publisher':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':' منتشر کننده' , 'style':'text-align: right!important;'}),
            # 'users':forms.ModelMultipleChoiceField(queryset=User.objects.all() , widget=forms.CheckboxSelectMultiple),
        }

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number' , 'username' , 'full_name' , 'email' , 'password' , 'password_copy')
        widgets={
            'phone_number':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':' شماره تلفن' , 'style':'text-align: right!important;'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder':' پسورد ' , 'style':'text-align: right!important;'}),
            'password_copy':forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder':'  تکرار پسورد ' , 'style':'text-align: right!important;'}),
            'username':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':' نام کاربری' , 'style':'text-align: right!important;'}),
            'full_name':forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام کامل' , 'style':'text-align: right!important;'}),
            'email':forms.EmailInput(attrs={'class': 'form-control' , 'placeholder':' ایمیل' , 'style':'text-align: right!important;'}),
        }

class CreateBrowssingForm(forms.ModelForm):
    class Meta:
        model = Borrowingbook
        fields = ('user' , 'book' , 'expiration_date')
