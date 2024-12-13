from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from store.views import *
urlpatterns = [
    path('', home, name = 'name'),
    path('products/<slug:slug>/',product,name='products'),
    path('single/<int:pk>/',single,name='single'),
]