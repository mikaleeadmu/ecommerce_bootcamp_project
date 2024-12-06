from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce_app.urls')),
     path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/update/', views.update_order_status, name='update_order_status'),
]
