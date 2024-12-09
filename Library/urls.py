from django.urls import path
from .views import *

app_name = 'library'

urlpatterns = [
    path('' , IndexView.as_view() , name='main'),
    path('search', SearchBookView.as_view(), name='search'),
    path('search_user', SearchUserView.as_view(), name='search_user'),
    #book
    path('create_book', CreateBookView.as_view(), name='add_book'),
    path('browssing_book', TestView.as_view(), name='briwssing_book'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book_edite/<int:pk>', book_edite, name='book_edite'),
    #user
    path('create_user' , CreateUserView.as_view() , name='add_user'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user_edite/<int:pk>', user_edite, name='user_edite'),
]