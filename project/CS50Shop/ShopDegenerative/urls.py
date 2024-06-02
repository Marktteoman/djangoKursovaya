from django.urls import path
from .views import PanCreateView, PanIpdateView, PaDeleteView, profile_view

app_name = 'ShopDegenerative'

urlpatterns = [
    path('profile', profile_view, name='profile'),
]