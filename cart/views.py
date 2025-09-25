from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from . cart_module import Cart
from .models import Order, OrderItem
from books.models import Book


class CartDetailView(View):
    def get(self , request):
        cart = Cart(self.request)
        return render(request, "cart/cart_detail.html", {'cart' : cart})
    
    def post(self, request):
        cart = Cart(self.request)
        return render(request, "cart/cart_detail.html", {'cart' : cart})
    

class CartAddView(View):
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        quantity = request.POST.get("quantity")

        cart = Cart(request)
        cart.add(book, quantity)
        return redirect('cart:cart_detail')
    


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart_detail')
    


class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order,id=pk)
        return render(request, "cart/order_detail.html", {'order' : order})


class OrderCreationView(View):
    def get(self,request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total_price())
        for item in cart:
            OrderItem.objects.create(order=order, book=item['book'], quantity=item['quantity'], price=item['price'])
            
        cart.remove_cart()

        return redirect("cart:order_detail", order.id)