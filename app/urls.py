from django.urls import path,include
from app import views
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
   
)
urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('users/register/',views.registerUser,name='register'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('product/',views.getProducts,name="getProducts"),
    path('product/<str:pk>/',views.getProduct,name="getProduct"),
    path('user/profile/',views.getUserProfiles,name="getUserProfiles"),
    path('product/electronics',views.electronics,name="electronics"),
     path('product/pricerange',views.pricerange,name="pricerange"),
          path('product/sports',views.Sports,name="sports"),
     path('product/menswear',views.Menswear,name="menswear"),
     path('product/womenswear',views.Womenswear,name="womenswear"),

    # path('products/<str:pk>',views.getProduct,name="getProduct"),
    path('users/',views.getUsers,name="getUsers"),
    path('users/<str:pk>/',views.getUserById,name="get_user"),
    path('users/profile/update/',views.updateUserProfile,name="user_profile_update"),
    path('users/update/<str:pk>/',views.updateUser,name="updateUser"),
    path('users/delete/<str:pk>/',views.deleteUser,name="deleteUser"),

  path('products/create/',views.createProduct,name="create_product"),
    path('products/upload/',views.uploadImage,name="upload_image"),

    path('products/<str:pk>/reviews/',views.createProductReview,name="create-review"),
    path('products/top/',views.getTopProducts,name="top-products"),

    path('products/update/<str:pk>/',views.updateProduct,name="update_product"),
    path('products/delete/<str:pk>/',views.deleteProduct,name="delete_product"),




    path('orders/',views.getOrders,name="allorders"),
    path('orders/add/',views.addOrderItems,name="orders-add"),
    path('orders/myorders/',views.getMyOrders,name="myorders"),

    path('orders/<str:pk>/deliver/',views.updateOrderToDelivered,name="delivered"),
    path('orders/<str:pk>/',views.getOrderById,name="user-order"),
    path('orders/<str:pk>/pay/',views.updateOrderToPaid,name="pay"),

]
