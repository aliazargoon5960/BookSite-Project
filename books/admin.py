from django.contrib import admin
from . models import Author , Category , Book , BookBaner

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author', 'category')

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(BookBaner)
