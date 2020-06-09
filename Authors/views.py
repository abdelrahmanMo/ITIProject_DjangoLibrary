from django.shortcuts import render,redirect,get_object_or_404
from .models import Authors
from .form import AuthorForm
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import booksSerializer
# Create your views here.

def all_authors(request):
    authors = Authors.objects.all()
    context = {
        'all_authors' : authors
    }
    return render(request,'authors/all_authors.html',context)

def author_details(request,id):
    author = get_object_or_404(Authors,id=id)
    context = {
        'author':author
    }
    return render(request,'authors/author_details.html',context)


def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST,request.FILES)
        if form.is_valid():
            new_form =form.save(commit=False)
            new_form.user =request.user
            new_form.save()
            return redirect('/authors')
    else:
        form =AuthorForm()
    context = {'form': form}
    return render(request, 'authors/create_author.html', context)

def edit_author(request,id):
    author = get_object_or_404(Authors,id=id)
    form =AuthorForm(request.POST,request.FILES,instance=author)
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/authors')
    else:
        form =AuthorForm(instance=author)
    context = {'form':form}
    return render(request,'authors/edit_author.html',context)

def delete_author(request, id):
    author = get_object_or_404(Authors , id=id)
    if request.method == "POST":
        author.delete()
        return redirect('/authors')
    context = {
        "author": author
    }
    return render(request, "authors/delete_author.html", context)

def search_author(request):
    if request.method == "POST":
        print(request.POST['search_inp'])
        author = get_object_or_404(Authors , authorName=request.POST['search_inp'])
        print(author.id)
        return redirect('/authors/'+str(author.id))
    else:
        return render(request,'authors/search_author.html')
class authorsList(APIView):
    def get(self,request):
        authors = Authors.objects.all()
        serializer = booksSerializer(authors,many=True)
        return Response(serializer.data)

    def Post(self):
        pass