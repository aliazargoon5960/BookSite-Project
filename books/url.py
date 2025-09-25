from django.urls import path
from . import views

app_name = 'books'
urlpatterns=[
    path('' , views.HomeView.as_view() , name='home'),
    path('book/<slug:slug>/' , views.BookDetailView.as_view() , name='book_detail'),
    path('author/<slug:slug>/' , views.AuthorDetailView.as_view() , name='author_detail'),
]