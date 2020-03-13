from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomSignupForm, CustomerForm, AddressForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
import stripe
from decouple import config

from .models import Restaurant

stripe.api_key = config('STRIPE_API_KEY')

# Create your views here.
def home(request):
    restaurants = Restaurant.objects
    return render(request, 'tables/home.html', {'restaurants':restaurants})

class SignUp(generic.CreateView):
    form_class = CustomSignupForm
    success_url = reverse_lazy('fillCustomer')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

def fillCustomer(request):
     if request.method == 'POST':
        filled_form = CustomerForm(request.POST)
        if filled_form.is_valid():
            created_customer = filled_form.save(commit=False)
            created_customer.user = request.user
            created_customer.save()

    #         created_pizza_pk = created_pizza.id
            filled_form = CustomerForm()
        else:
            created_customer_pk = None
    #         note = 'Order was not created, please try again'
        #print ("customer post")
        address_form = AddressForm()
        return render(request, 'registration/address.html', {'form':address_form})
     else:
        #print ("customer get")
        customer_form = CustomerForm()
        return render(request, 'registration/customer-registration.html', {'form':customer_form})

def fillAddress(request):
    # if request.method == 'POST':
        filled_form = AddressForm(request.POST)
        print ("Address post")
        if filled_form.is_valid():
            created_address = filled_form.save()
        #    created_address_pk = created_address.id
        #    note = 'Address Saved!'
            print ('Address saved')
            filled_form = AddressForm()
        else:
            created_address_pk = None
        #    note = 'Order was not created, please try again'
            print ('Not valid form')
        return render(request, 'tables/home.html')
    # else:
    #     print ("Address get")
    #     address_form = AddressForm()
    #     return render(request, 'registration/address.html', {'form':address_form})

def join(request):
    return render(request, 'tables/join.html')