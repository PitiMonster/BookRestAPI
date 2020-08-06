from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.BooksView.as_view(), name='books_view'),
    re_path(r'^(?P<bookId>\d+)/', views.BooksView.as_view(), name='books_view'),
]