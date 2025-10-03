from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView , ListView , FormView , UpdateView , DetailView , View
from django.db.models import Q
from Library.models import Book , Borrowingbook
from account.models import User
from .forms import CreateBookForm , CreateUserForm

class IndexView(TemplateView):
    template_name = 'Library/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['users'] = User.objects.all()
        context['browsing_book'] = Borrowingbook.objects.all()
        context['borrowing_books'] = Book.objects.filter(browssing=True)
        return context

class SearchBookView(ListView):
    template_name = 'Library/search-result.html'
    model = Book
    paginate_by = 15
    context_object_name = 'books'
    def get_queryset(self):
        q = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=q) | Q(content__icontains=q) | Q(created_at__icontains=q) | Q(publisher__icontains=q) | Q(educational_base__icontains=q))

class SearchUserView(ListView):
    template_name = 'Library/search-user-result.html'
    model = User
    paginate_by = 15
    context_object_name = 'users'
    def get_queryset(self):
        q = self.request.GET.get('q2')
        return User.objects.filter(
            Q(phone_number__icontains=q) | Q(username__icontains=q) | Q(email__icontains=q) | Q(full_name__icontains=q))
    
class SearchBorrowingView(ListView):
    template_name = 'Library/search-result-borrowing.html'
    model = User
    paginate_by = 15
    context_object_name = 'browsing_book'
    def get_queryset(self):
        q = self.request.GET.get('q3')
        return User.objects.filter(
            Q(full_name__icontains=q) | Q(phone_number__icontains=q))
    

class CreateBookView(FormView):
    template_name = 'Library/add_book.html'
    form_class = CreateBookForm
    success_url = 'library:main'
    def form_valid(self , form):
        cd = form.cleaned_data
        form.save()
        return redirect(reverse('library:main'))

class BookDetailView(DetailView):
    template_name = 'Library/book-detail.html'
    model = Book
    context_object_name = 'book'

def book_edite(request , pk):
    if request.user.is_authenticated == True:
        user = request.user
        book = get_object_or_404(Book , pk=pk)
        form = CreateBookForm(instance=book)
        if request.method == 'POST':
            form = CreateBookForm(request.POST  , request.FILES , instance=book)
            if form.is_valid():
                form.save()
                return redirect('library:main')
        else:
            form = CreateBookForm(instance=book)
        return render(request , 'Library/book-edite.html' , {'form':form})
    else:
        return redirect('library:main')
    
class BookDelete(View):
    def get(self , request , pk):
        book = get_object_or_404(Book , pk=pk)
        book.delete()
        return redirect('library:main')
     
class CreateUserView(FormView):
    template_name = 'Library/add_user.html'
    form_class = CreateUserForm
    success_url = 'library:main'
    def form_valid(self , form):
        cd = form.cleaned_data
        form.save()
        return redirect(reverse('library:main'))

class UserDetailView(DetailView):
    template_name = 'Library/user-detail.html'
    model = User
    context_object_name = 'user'

def user_edite(request , pk):
    if request.user.is_authenticated == True:
        user = get_object_or_404(User , pk=pk)
        form = CreateUserForm(instance=user)
        if request.method == 'POST':
            form = CreateUserForm(request.POST  , request.FILES , instance=user)
            if form.is_valid():
                form.save()
                return redirect('library:main')
        else:
            form = CreateUserForm(instance=user)
        return render(request , 'Library/user-edite.html' , {'form':form})
    else:
        return redirect('library:main')

class UserDelete(View):
    def get(self , request , pk):
        user = get_object_or_404(User , pk=pk)
        user.delete()
        return redirect('library:main')
    
class BrowssingView(View):
    template_name = 'Library/briwssing_book.html'
    def get(self , request):
        books = Book.objects.filter(browssing=False)
        return render(self.request , self.template_name , {'books':books})

class BrowssingFormView(View):
    template_name = 'Library/briwssing_book.html'
    def post(self , request):
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        book = request.POST.get('book')
        expiration_date = request.POST.get('expiration_date')
        books = Book.objects.all()
        for x in books:
            book_name = f'{x.title}--{x.educational_base}--{x.leason.title}--{x.publisher}'
            if book_name == book:
                print(x)
                x.browssing == True
                y=x
        book = Borrowingbook.objects.create(full_name=full_name , phone_number=phone_number , expiration_date=expiration_date)
        book.book.add(y)
        return redirect('library:main')
    
class BorrowingDelete(View):
    def get(self , request , pk):
        book = get_object_or_404(Borrowingbook , pk=pk)
        book.delete()
        return redirect('library:main')
