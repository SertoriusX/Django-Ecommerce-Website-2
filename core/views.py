from django.shortcuts import render,redirect
from django.db.models import Q
from product.models import Product,Category
from django.core.paginator import Paginator
from .forms import SingUpForm
from django.contrib.auth import login
# Create your views here.
def frontpage(request):
    products =Product.objects.all()[0:8]
    paginator = Paginator(Product.objects.all(), 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
    return render(request,'core/frontpage.html',{"products":products})

def signup(request):
    if request.method =="POST":
        form=SingUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            
            login(request,user)
            return redirect('/')
    else:
        form=SingUpForm()
    return render(request,'core/signup.html')

def login_old(request):
    return render(request,'core/login.html')

def shop(request):
    categories=Category.objects.all()
    products =Product.objects.all()
    active_category =request.GET.get('category','')
    
    if active_category:
        products =products.filter(category__slug=active_category)
    query=request.GET.get('query','')
    if query:
        products =products.filter(Q(name__icontains=query)|Q(description__icontains=query))
        
 
    ctx={"categories":categories,
         "products":products,
          "active_category":active_category,
          }
    return render(request,'core/shop.html',ctx)


