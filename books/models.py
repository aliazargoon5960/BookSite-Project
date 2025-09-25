from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Author(models.Model):
    fullname = models.CharField(max_length=50) 
    age = models.CharField(max_length=3, null=True, blank=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)
    slug = models.SlugField(unique=True ,null=True , blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('books:author_detail', args=[self.slug])
    

    def __str__(self):
        return self.fullname


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,blank=True, null=True)
    author = models.ForeignKey(Author , on_delete=models.CASCADE , related_name='books')
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/' , null=True , blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name='books')
    published_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args , **kwargs)
    
    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.slug])
    
    def __str__(self):
        return self.title
    


class BookBaner(models.Model):
    title_baner = models.CharField(max_length=50)
    author_baner = models.ForeignKey(Author , on_delete=models.CASCADE)
    price_baner = models.IntegerField()
    image_baner = models.ImageField(upload_to='books/' , null=True , blank=True)
    description_baner = models.TextField()
    category_baner = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date_baner = models.DateField()

    def __str__(self):
       return self.title_baner