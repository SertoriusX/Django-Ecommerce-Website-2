"""tsvetan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from core.views import frontpage,shop,signup,login_old
from product.views import product
from cart.views import add_to_cart,cart,checkout
from django.contrib.auth import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',frontpage,name='frontpage'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('login/',views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('cart/',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('shop/',shop,name='shop'),
    path('signup/',signup,name='signup'),
    path('login/',login_old,name="login"),
    path('shop/<slug:slug>',product,name='product'),
    path('add_to_cart/<int:product_id>',add_to_cart,name='add_to_cart')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)