from django.urls import path

from api import cart_views, orders_views, products_views, users_views

urlpatterns = [
    path('v1/categories/', products_views.CategoryAPIView.as_view(), name='category-list'),
    path('v1/products/', products_views.ProductAPIView.as_view(), name='product-list'),
    path('v1/products/<slug:slug>/', products_views.ProductDetailView.as_view(), name='product-detail'),
    path('v1/new-products/', products_views.NewProductsAPIView.as_view(), name='new-product'),
    path('v1/recommended-products/', products_views.RecommendedProductsAPIView.as_view(), name='recommended-product'),
    path('v1/profile/', users_views.ProfileViewSet.as_view({'get': 'me'}), name='profile'),
    path('v1/profile/update/', users_views.ProfileViewSet.as_view({'patch': 'me'}), name='profile-update'),
    path('v1/cart/', cart_views.CartAPIView.as_view(), name='cart'),
    path('v1/cart/add/', cart_views.AddToCartAPIView.as_view(), name='add-to-cart'),
    path('v1/cart/remove/', cart_views.RemoveFromCartAPIView.as_view(), name='remove-from-cart'),
    path('v1/cart/clear/', cart_views.ClearCartAPIView.as_view(), name='clear-cart'),
    path('v1/order/', orders_views.OrderDetailAPIView.as_view(), name='orders'),
    path('v1/order/create/', orders_views.OrderCreateAPIView.as_view(), name='create-order'),
    path('v1/user-orders/', orders_views.UserOrderListAPIView.as_view(), name='user-orders'),
]
