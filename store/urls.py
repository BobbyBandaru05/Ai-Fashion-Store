from django.urls import path
from .views import (
    home,
    product_detail,
    cart,
    checkout,
    success,
    men,
    women,
    add_to_cart,
    remove_from_cart,
    register_page,
    login_page,
    logout_page,
    orders,
    accessories
)

urlpatterns = [

    path('', home, name='home'),
    path('product/<int:id>/', product_detail, name='product_detail'),

    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('success/', success, name='success'),

    path('men/', men, name='men'),
    path('women/', women, name='women'),

    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>/', remove_from_cart, name='remove_from_cart'),

    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),

    path('orders/', orders, name='orders'),
    path('accessories/',accessories,name='accessories'),
]