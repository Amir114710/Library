from typing import Iterable
from django.db import models
from account.models import User
from persiantools.jdatetime import JalaliDate
from django.utils.text import slugify

class Type(models.Model):
    title = models.CharField(max_length=350 , null=True , verbose_name='نوع کتاب')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'نوع کتاب'
        verbose_name_plural = 'نوع کتاب ها'

class Leason(models.Model):
    title = models.CharField(max_length=350 , null=True , verbose_name='نام درس')
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'درس'
        verbose_name_plural = 'درس ها'

class Category(models.Model):
    title = models.CharField(max_length=250 , null=True , verbose_name='نام دسته بندی')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Book(models.Model):
    title = models.CharField(max_length=250 , null=True , verbose_name='نام کتاب')
    content = models.TextField(null=True , verbose_name='توضیحات')
    created_at = models.IntegerField(null=True , verbose_name='سال انتشار')
    category = models.ManyToManyField(Category , related_name='books_category' , null=True , verbose_name='نوع کتاب')
    leason = models.ForeignKey(Leason , on_delete=models.CASCADE , related_name='books_leason' , null=True , verbose_name='درس')
    type = models.ManyToManyField(Type , related_name='books_type' , null=True , verbose_name=' سطح')
    publisher = models.CharField(max_length=450 , null=True , verbose_name='ناشر')
    the_author = models.TextField(null=True , verbose_name='مولفان')
    educational_base = models.CharField(max_length=350 , null=True , verbose_name='پایه تحصیلی')
    users = models.ManyToManyField(User , related_name='books_user' , null=True , verbose_name='کاربران')
    image = models.FileField(upload_to='book/image' , blank=True , null=True , verbose_name='تصویر کتاب')  
    status = models.BooleanField(default=True , verbose_name='موجودی')
    browssing = models.BooleanField(default=False , verbose_name='امانت')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}---{self.educational_base}-----{self.leason.title}'
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها '

    def get_jalali_date(self):
        return JalaliDate(self.created, locale=('fa')).strftime("%c")
    
class Borrowingbook(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='rents' , null=True , blank=True , verbose_name='کاربر')
    book = models.ManyToManyField(Book , related_name='rents' , null=True , blank=True , verbose_name='کتاب')
    expiration_date = models.DateTimeField(null=True , blank=True , verbose_name='تاریخ انقضا')
    date_added = models.DateTimeField(auto_now_add=True , verbose_name='تاریخ تولید')

    def __str__(self) -> str:
        return f'{self.user.phone_number}---{self.book.title}'

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'امانت'
        verbose_name_plural = 'امانت ها '

    def get_jalali_date(self):
        return JalaliDate(self.date_added , self.expiration_date , locale=('fa')).strftime("%c")
