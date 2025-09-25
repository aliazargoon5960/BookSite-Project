from django.shortcuts import render
from . forms import LoginForm , RegisterForm , AddressCreationForm
from django.views import View
from django.contrib.auth import authenticate , login
from django.shortcuts import redirect
from django.contrib.auth import logout
from . models import User



# def user_login(request):
#     return render(request, "account/login.html", {})


class UserLogin(View):
    def get(self,request):
        form = LoginForm()
        return render(request , "account/login.html", {'form' : form})
    

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'] , password=cd['password'])
            if user is not None:
                login(request,user)
                return redirect('books:home')
            else:
                form.add_error('username' , 'invalid user data...')

        else:
            form.add_error('username', 'invalid data...')

        return render(request , "account/login.html", {'form' : form})
    



class UserRegister(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, 'account/register.html' , {'form' : form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(phone=phone , password=password)
            user.backend = 'account.authentication.EmailAuthBackend'
            login(request,user)
            return redirect('books:home')
        
        return render(request, 'account/register.html' , {'form' : form})



class AddAddressView(View):
    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
           address = form.save(commit=False)
           address.user = request.user
           address.save()
           next_page = request.GET.get('next')
           if next_page:
               return redirect(next_page)

        
        return render(request, "account/add_address.html", {'form' : form})
    
    def get(self, request):
        form = AddressCreationForm()
        return render(request, "account/add_address.html", {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('books:home')