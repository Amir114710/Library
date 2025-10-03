from django.urls import path
from .views import *

app_name = 'library'

urlpatterns = [
    path('' , IndexView.as_view() , name='main'),
    path('search', SearchBookView.as_view(), name='search'),
    path('search_user', SearchUserView.as_view(), name='search_user'),
    path('search_borrowing', SearchBorrowingView.as_view(), name='search_borrowing'),
    #book
    path('create_book', CreateBookView.as_view(), name='add_book'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book_edite/<int:pk>', book_edite, name='book_edite'),
    path('book/delete/<int:pk>' , BookDelete.as_view() , name='book_delete'),
    path('browssing_book', BrowssingView.as_view(), name='briwssing_book'),
    path('browssing_book/add', BrowssingFormView.as_view(), name='briwssing_form_book'),
    path('borrowing/delete/<int:pk>' , BorrowingDelete.as_view() , name='borrowing_delete'),
    #user
    path('create_user' , CreateUserView.as_view() , name='add_user'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user_edite/<int:pk>', user_edite, name='user_edite'),
    path('user/delete/<int:pk>' , UserDelete.as_view() , name='user_delete')
]