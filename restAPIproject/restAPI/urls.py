from django.urls import re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    re_path(r'^books/$', views.BooksView.as_view(), name='books_view_get'),
    re_path(r'^books/(?P<bookId>\d+)/', views.BooksView.as_view(), name='books_view'),
    re_path(r'^db/$', TemplateView.as_view(template_name='restAPI/postView.html')),
    re_path(r'^db/handle_data/$', views.BooksView.as_view(), name='books_view_post'),
]