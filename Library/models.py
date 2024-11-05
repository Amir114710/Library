from django.db import models
from django.contrib.auth.models import User
from persiantools.jdatetime import JalaliDate

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
    category = models.ManyToManyField(Category , related_name='books_category' , null=True , verbose_name='دسته بندی')
    leason = models.ForeignKey(Leason , on_delete=models.CASCADE , related_name='books_leason' , null=True , verbose_name='درس')
    type = models.ManyToManyField(Category , related_name='books_type' , null=True , verbose_name='نوع کتاب')
    publisher = models.CharField(max_length=450 , null=True , verbose_name='ناشر')
    the_author = models.TextField(null=True , verbose_name='مولفان')
    educational_base = models.CharField(max_length=350 , null=True , verbose_name='پایه تحصیلی')
    users = models.ManyToManyField(User , related_name='books_user' , null=True , verbose_name='کاربران')
    image = models.FileField(upload_to='book/image' , null=True , verbose_name='تصویر کتاب')  
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}---{self.educational_base}-----{self.leason.title}'
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها '

    def get_jalali_date(self):
        return JalaliDate(self.created, locale=('fa')).strftime("%c")