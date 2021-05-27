from django.contrib import admin
from django.urls import path
from .views import home, login, signup
from .views.login import logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView

urlpatterns = [
    path('', home.Index.as_view(), name="homepage"),
    path('signup', signup.Signup.as_view(), name="signup"),
    path('login', login.Login.as_view(),  name="login"),
    path('logout', logout,  name="logout"),
    path('cart', Cart.as_view(),  name="cart"),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders')
]
