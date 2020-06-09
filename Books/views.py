from django.shortcuts import render,get_object_or_404,redirect
from .models import Books,status
from .form import BooksForm
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import booksSerializer
# Create your views here.

def all_books(request):
    #books = Books.objects.filter(statusName=1)
    books = Books.objects.all()
    context ={
        'all_books' : books
    }
    return render(request,'books/all_books.html',context)

def create(request):
    if request.method == 'POST':
        form = BooksForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.User=request.user
            new_form.save()
            return redirect('/books')
    else:
        form = BooksForm()
    context = {
        'form':form
    }
    return render(request,'books/create.html',context)

def book_detail(request,id):
    book = get_object_or_404(Books,id= id)
    context = {
        'book':book,
    }
    return render(request,'books/book_detail.html',context)

def edit(request,id):
    book = get_object_or_404(Books,id=id)
    if request.method == 'POST':
        form = BooksForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/books')
    else:
        form = BooksForm(instance=book)

    context = {
        'form': form
    }
    return render(request, 'books/edit.html', context)
def delete(request, id):
    book = get_object_or_404(Books , id=id)
    if request.method == "POST":
        book.delete()
        return redirect('/books')
    context = {
        "book": book
    }
    return render(request, "books/delete.html", context)

def search_book(request):
    if request.method == "POST":
        print(request.POST['search_inp'])
        book = get_object_or_404(Books , Name=request.POST['search_inp'])
        print(book.id)
        return redirect('/books/'+str(book.id))
    else:
        return render(request,'books/search_book.html')
class booksList(APIView):
    def get(self,request):
        books = Books.objects.all()
        serializer = booksSerializer(books,many=True)
        return Response(serializer.data)


    def Post(self):
        pass
