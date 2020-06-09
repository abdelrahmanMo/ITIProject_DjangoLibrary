from django.conf.urls import url
from .  import views
app_name = 'Authors'
urlpatterns=[
    url(r'^$',views.all_authors,name='all_authors'),
    url(r'^create$',views.create_author,name='create_author'),
    url(r'^(?P<id>\d+)$',views.author_details,name='author_details'),
    url(r'^(?P<id>\d+)/edit$', views.edit_author, name='edit_author'),
    url(r'^(?P<id>\d+)/delete$', views.delete_author, name='delete_author'),
    url(r'^search$',views.search_author,name='search_author'),
    url(r'^authorapi', views.authorsList.as_view()),
]