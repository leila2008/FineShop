from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Наименование категории',max_length=255,unique=True)
    description = models.TextField(verbose_name='Описание категории',max_length=500,blank=True)
    created = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True,)
    modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True,)
    parents = models.ForeignKey('self', on_delete=models.PROTECT, null=True, related_name='parent')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'

   
class Product(models.Model):
    category = models.ForeignKey(Category,verbose_name='Категория',on_delete=models.CASCADE,related_name='category')
    name = models.CharField(verbose_name='Наименование',max_length=128)
    description = models.TextField(verbose_name='Описание',blank=True)
    specifications = models.TextField( verbose_name='Характеристики',blank=True)
    price_now = models.DecimalField(verbose_name='Текущая цена',max_digits=8,decimal_places=2,default=0)
    price_old = models.DecimalField(verbose_name='Предыдущая цена',max_digits=8,decimal_places=2,default=0)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе',default=0)
    image = models.ImageField(upload_to='products_images',blank=True)

    def __str__(self):
        return f"​{self.name}​ (​{self.category.name}​)"
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class CartProduct(models.Model):
    cart = models.ForeignKey('Cart', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"(self.product.name) - (self.quantity)"

    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for (self.user)"
    
class Region(models.Model):
    city = models.CharField(max_length = 255)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True , null = True, upload_to= 'user/avatar')
    birth_day = models.DateField(blank= True, null=True)
    region = models.ForeignKey(Region ,blank = True, null = True, on_delete = models.PROTECT)

    def __str__(self):
        return self.user.username
    
class Brand(models.Model):
    pass

class Post(models.Model):
    pass

class Comment(models.Model):
    pass

