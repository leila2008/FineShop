from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from da.models import Product,Category, Cart,Profile,Post, Post_Category,CartProduct
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.http import HttpResponseRedirect

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
    category = get_object_or_404(Category, id=id)
    return render(request, 'category_detail.html', {'category': category})

def profile(request, id):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

def cart(request, id):
    cart = get_object_or_404(Cart, id=id)
    return render(request, 'cart.html',{'cart': cart,})

def add_item_cart(request, id):
    item = CartProduct()
    product = Product.objects.get(id=id)
    item.product = product
    cart = Cart.objects.get(user=request.user)
    cart.items.add(item)
    cart.save()
    return redirect('cart') 

def delete_item_cart(request, id):
    item = Cart.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/cart/')

def edit_item_cart(request, id):
    item = CartProduct.objects.get(id=id)
    cart = Cart.objects.get(user=request.user)
    
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        cart_item = CartProduct.objects.get(item=item, cart=cart)
        cart_item.quantity = quantity
        cart_item.save()
        return redirect('cart')
    return render(request, 'edit_item_cart.html', {'item': item,'cart': cart})
    
    
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})
    
def post_detail(request, slug):
    post = Post.objects.get(slug__exact=slug)
    return render(request, 'post_detail.html', {'post': post})

def posts(request):
    posts = Post.objects.filter()
    return render(request,'post.html', {'posts': posts})

def post_categories(request):
    post_categories = Post_Category.objects.all()
    return render(request, 'post_categories.html' , {'post_categories':post_categories })

def post_category(request, slug):
    post_category = Post_Category.objects.get(slug__exact=slug)
    return render(request, 'post_category.html', {'post_category': post_category})

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                profile = Profile()
                profile.user = user
                profile.save()
                login(request, user)
                return redirect('index')
        else:
            form = RegisterForm()
        return render(request , 'register.html' , {'form': form})
    return redirect('index')

def login_site(request):
    if request.user.is_authenticated:
        return redirect('index')
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            message = 'Извините, такого пользователя не существует'
            return render(request, "login.html", {'message': message})
    return render(request, 'login.html')

def logout_site(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')