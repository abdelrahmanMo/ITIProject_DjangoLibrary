from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'Books'
urlpatterns=[
    url(r'^$',views.all_books,name='all_books'),
    url(r'^create$', views.create ,name='create'),
    url(r'^(?P<id>\d+)$', views.book_detail ,name='book_detail'),
    url(r'^(?P<id>\d+)/edit$', views.edit, name='edit'),
    url(r'^(?P<id>\d+)/delete$', views.delete, name='delete'),
    url(r'^search$',views.search_book,name='search_book'),
    url(r'^bookapi', views.booksList.as_view()),
]