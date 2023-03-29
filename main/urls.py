from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homepage, name = "home"),
    path('products', views.product, name = "products"),
    path('category/<str:id>/<slug:slug>', views.category, name = "category"),
    path('detail/<str:id>/<slug:slug>', views.detail, name = "detail"),
    path('contact', views.contact, name = "contact"),
    path('signout', views.signout, name = "signout"),
    path('signin', views.signin, name = "signin"),
    path('register', views.register, name='signup'),
    path('search', views.search, name='search'),
    path('profile', views.profile, name='profile'),
    path('profile_update', views.profile_update, name='profile_update'),
    path('password_update', views.password_update, name='password_update'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('checkout', views.checkout, name='checkout'),
    path('payment', views.payment, name='payment'),
    path('callback', views.callback, name='callback'),
]

