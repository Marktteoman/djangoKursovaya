from django.urls import path
from .views import register
from ShopDegenerative.views import index, indexItem

app_name = 'Users'

urlpatterns = [
    path('register/', register, name='register'),

]

