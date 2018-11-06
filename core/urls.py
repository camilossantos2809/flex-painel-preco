from django.urls import path
from .views import (index, screen_promotion, add_promotion,
                    list_promotions, add_screen, list_products)

urlpatterns = [
    path('', index),
    path('<int:screen>/promotion', screen_promotion, name='promotion'),
    path('screen/add', add_screen, name="add_screen"),
    path('promotion/add', add_promotion, name="add_promotion"),
    path('promotions', list_promotions, name="promotions"),
    path('products', list_products, name='list_products'),
]
