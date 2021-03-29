from django.urls import path, re_path
from .views import HomeView, AboutView, ProductView


app_name = 'auction'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('product/<int:id>/', ProductView.as_view(), name='product')
]

