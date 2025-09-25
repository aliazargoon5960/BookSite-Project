from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from . models import Book , BookBaner , Category , Author
from django.core.paginator import Paginator

# class HomeView(TemplateView):
#     template_name = 'books/book_list.html'


# class BaseListView(ListView):
#     model = Book
#     template_name = 'books/book_list.html'
#     context_object_name = 'books'


class HomeView(TemplateView):
    template_name = 'books/book_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_books = Book.objects.all()
        paginator = Paginator(all_books, 4)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['books'] = page_obj
        context['page_obj'] = page_obj
        context['cheapest_book'] = Book.objects.order_by('price').first()
        context['banners'] = BookBaner.objects.all() 
        context['categories'] = Category.objects.all()
        context['active_category'] = None  
        context['authors'] = Author.objects.all()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_detail.html'
    context_object_name = 'author'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.object)
        return context