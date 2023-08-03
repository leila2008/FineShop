from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    # path('product', views.product, name='product'),
    # path('categories' ,  views.category , name = 'categories'),
    path('search/', views.search_function, name = 'search'),
]