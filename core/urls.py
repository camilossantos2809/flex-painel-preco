from django.urls import path
from .views import (index, screen_promotion, add_promotion,
                    list_promotions, add_screen, list_products, screen_prices_list)

urlpatterns = [
    path('', index),
    path('screen/promotion/<int:screen>', screen_promotion, name='screen_promotion'),
    path('screen/prices-list/<int:screen>', screen_prices_list, name='screen_prices_list'),
    path('screen/add', add_screen, name="add_screen"),
    path('promotion/add', add_promotion, name="add_promotion"),
    path('promotion/edit/<int:id>', add_promotion, name="edit_promotion"),
    path('promotions', list_promotions, name="promotions"),
    path('products', list_products, name='list_products'),
]
