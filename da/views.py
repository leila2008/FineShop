from django.shortcuts import render
from .models import Product,Category

# Create your views here.

def index(request):
    categorys = Category.objects.all()
    return render (request, 'index.html', { 'category': categorys} )

def search_function(request):
    query = request.GET.get('search')
    posts = Product.objects.filter(query(title__icontains=query))
    context = {'query': query, 'posts': posts}
    return render(request, 'search.html' , context)

def category_detail(request, id):
    pass

def profile(request, id):
    pass

def about(request):
    pass

def cart(request, id):
    pass

def product_detail(request, id):
    pass
