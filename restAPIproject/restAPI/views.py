from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Book
from .serializers import BookSerializer

class BooksView(APIView):

    def get(self, request, bookId : int = None):

        # if bookId provided then return specified book
        if bookId is not None:
            book = get_object_or_404(Book, pk=int(bookId))
            response = BookSerializer(book).data
            return Response({'response':response})

        # otherwise return book set depending on other parameters
        all_books = Book.objects.all()

        authors = request.query_params.getlist('author')            # extract all authors
        dates = request.query_params.getlist('published_date')      # extract all dates
        sort = request.query_params.get('author', 'published_date') # extract sort type

        if authors:
            res_authors = Book.objects.none()

            # combine all authors qss into one qs
            for a in authors:
                curr_author_books = all_books.filter(authors__contains=a)
                res_authors |= curr_author_books

            all_books = res_authors

        if dates:
            res_dates = Book.objects.none()

            # combine all dates qss into one qs
            for d in dates:
                curr_date_books = all_books.filter(published_date=d)
                res_dates |= curr_date_books

            all_books = res_dates

        if sort != 'published_date':
            all_books.order_by(sort)

        response = BookSerializer(all_books, many=True).data
        return Response({'response':response})