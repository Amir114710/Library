from django.urls import path
from .views import IndexView

app_name = 'library'

urlpatterns = [
    path('' , IndexView.as_view() , name='main'),
]