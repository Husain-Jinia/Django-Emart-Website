
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# Create your views here.
def index(request):

    products = None
    categories = Category.get_all_categories()
    CategoryID = request.GET.get('category')
    if CategoryID:
        products = Product.get_all_products_by_categoryid(CategoryID)
    else:
        products= Product.get_all_products()
    data = {}
    data['products']= products
    data['categories'] = categories
    return render(request, 'index.html', data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        #validation
        value ={
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone = phone,
                                email= email,
                                password=password)

        if(not first_name):
            error_message= "First name required"
        elif len(first_name) < 4:
            error_message = "First Name must be 4 character long or more"
        elif not last_name:
            error_message="Last name required"
        elif len(last_name) < 4 :
            error_message="last name must be atleast 4 characters"
        elif not phone:
            error_message="Phone number is required"
        elif len(phone) > 10:
            error_message= "phone number should not exceed 10 characters"
        elif len(password) < 6:
            error_message = "Password must be atleast 6 character long"
        elif len(email) < 5:
            error_message = "Email must be atleast 5 character long"
        elif customer.isExists():
            error_message = 'Email Address already registered . . '
        
        
        print(first_name, last_name, phone, email, password)
        
            
        
        if not error_message:
            

            
            customer.register()

            return redirect('homepage')
        else:
            data ={
                'error': error_message,
                'values' : value
            }
            return render(request, 'signup.html', data )
