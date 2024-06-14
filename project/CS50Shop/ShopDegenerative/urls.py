from django.urls import path
from .views import *

app_name = 'ShopDegenerative'

urlpatterns = [
    path('', index),
    path('cats/<int:catId>/', categories)
]

