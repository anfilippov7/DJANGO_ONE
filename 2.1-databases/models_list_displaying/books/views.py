from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books.html'
    books_objects = Book.objects.all()
    print(books_objects)
    print(books_objects.query)
    context = {
        'books': books_objects,
    }
    return render(request, template, context)


def book_view(request, pub_date):
    template = 'books/book.html'
    book_objects = Book.objects.all()
    print(str(book_objects.query))
    book_pub_date = Book.objects.filter(pub_date=pub_date)
    id_pub_date = [f'{book.id}' for book in book_pub_date][0]
    CONTENT = [book for book in book_objects]
    page_number = request.GET.get('page', id_pub_date)
    paginator = Paginator(CONTENT, 1)
    page = paginator.get_page(page_number)
    book_id = [f'{book.id}' for book in page.object_list][0]
    book_next = Book.objects.filter(id=int(book_id[0]) + 1)
    try:
        next_pub_date = [f'{book.pub_date}' for book in book_next][0]
    except:
        next_pub_date = None
    book_previous = Book.objects.filter(id=int(book_id[0]) - 1)
    try:
        previous_pub_date = [f'{book.pub_date}' for book in book_previous][0]
    except:
        previous_pub_date = None
    context = {
        'page': page,
        'book': page.object_list,
        'next': next_pub_date,
        'previous': previous_pub_date,
    }
    return render(request, template, context)


