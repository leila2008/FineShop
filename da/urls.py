from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('search/', views.search_function, name = 'search'),
    path('posts/', views.posts, name='posts'),
    path('post_categories/' ,  views.post_categories , name = 'post_categories'),
    path('post_category/' ,  views.post_category , name = 'post_category'),
    path('profile/', views.profile,name='profile'),
    path('cart/',views.cart,name='cart'),
    path('product_detail/',views.product_detail,name='product_detail'),
    path('register/' ,  views.register , name = 'register'),
    path('login/' ,  views.login_site , name = 'login_url'),
    path('logout/' ,  views.logout_site , name = 'logout_url'),
    path('about/', views.about,name='about'),
    path('add_item_cart/',views.add_item_cart, name='add_item_cart'),
    path('delete_item_cart/', views.delete_item_cart, name='delete_item_cart'),
    path('edit_item_cart/',views.edit_item_cart,name='edit_item_cart'),
    path('category_detail/',views.category_detail,name='category_detail'),
]