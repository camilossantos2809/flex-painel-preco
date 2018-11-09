from django.urls import path

from .views import (add_promotion, add_screen, delete_promotion, index,
                    list_products, list_promotions, screen_prices_list,
                    screen_promotion)

urlpatterns = [
    path('', index),
    path('screen/promotion/<int:screen>',
         screen_promotion, name='screen_promotion'),
    path('screen/prices-list/<int:screen>',
         screen_prices_list, name='screen_prices_list'),
    path('screen/add', add_screen, name="add_screen"),
    path('promotion/add', add_promotion, name="add_promotion"),
    path('promotion/edit/<int:id>', add_promotion, name="edit_promotion"),
    path('promotion/delete/<int:id>', delete_promotion, name="delete_promotion"),
    path('promotions', list_promotions, name="promotions"),
    path('products', list_products, name='list_products'),
]
