from django.urls import path
from ShopDegenerative.views import index, indexItem

app_name = 'ShopDegenerative'

urlpatterns = [
    path('', index),
    path('<int:my_id>/', indexItem, name="detail"),

]

