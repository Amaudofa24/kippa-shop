from django.urls import path

from .import views


app_name = 'totes'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('tote/<slug:slug>/', views.product_detail, name='product_detail'),
]
