from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Book
from .serializers import BookSerializer
from .utils import find_values

class BooksView(APIView):

    def get(self, request, bookId : int = None):

        # if bookId provided then return specified book
        if bookId is not None:
            book = get_object_or_404(Book, pk=int(bookId))
            response = BookSerializer(book).data
            return Response({'response':response}, status=status.HTTP_200_OK)

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
        return Response({'response':response}, status=status.HTTP_200_OK)

    def post(self, request):

        # extract data
        data = request.data['data']

        try:
            # if data contains list of books
            items = data['items']
        except:
            # if data contains one book
            if isinstance(items, list):
                items = data
            else:
                items = list(data)

        for i in items:
            # template of book's data
            book_data = {'title': None, 'published_date': None, 
                        'authors': None, 'categories': None, 
                        'average_rating': None, 'ratings_count': None, 
                        'thumbnail': None
                        }
            # fill book_data with incoming data
            book_data = find_values(data, book_data)

            book = Book(book_data)
            
            if book.is_valid():
                book.save()
            else:
                response = 'Wrong data provided!'
                return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        response = 'Completed successfully'
        return Response(response, status=status.HTTP_201_CREATED)
