from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'product', views.ProductSerializer)
router.register(r'order', views.OrderSerializer)
router.register(r'orderItem', views.OrderItemSerializer)
router.register(r'ShippingAddress', views.ShippingAddressSerializer)

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('token/', obtain_auth_token, name='api_token_auth'),
]