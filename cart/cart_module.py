from books.models import Book


CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = {}
            self.session[CART_SESSION_ID] = cart

        self.cart = cart
    
    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            book = Book.objects.get(id=int(item['id']))
            item['book'] = book
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_id_generator(book.id)
            yield item

    def unique_id_generator(self, id):
        result = f'{id}'
        return result
    
    def remove_cart(self):
        del self.session[CART_SESSION_ID]

    def add(self, book, quantity):
        unique = self.unique_id_generator(book.id)

        if unique not in self.cart:
            self.cart[unique] = {'quantity':0, 'price':str(book.price), 'id':book.id}
        
        self.cart[unique]['quantity'] += int(quantity)
        self.save()
    
    def total_price(self):
        cart = self.cart.values()
        total = sum(int(item['price']) * int(item['quantity']) for item in cart)
        return total
    
    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def save(self):
        self.session.modified = True