from django.urls import include, path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    path("cart/<user>", views.user_cart, name='cart'),
    path("orders/<user>", views.user_orders, name='orders'),
    path("yourorders/<int:cart_id>", views.previousorders, name='previousorders'),
    path("clear", views.clear, name='clear'),
    path("order", views.order, name='order'),
    path("addpizza", views.addpizza, name="addpizza"),
    path("addsub", views.addsub, name="addsub"),
    path("addsaladpasta", views.addsaladpasta, name="addsaladpasta"),
    path("adddinplat", views.adddinplat, name="adddinplat"),
]
