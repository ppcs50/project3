from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum

from .forms import SignUpForm
from .models import Type, Size, Style, Topping, Pizza, Sub, SaladPasta, Dinplat, Cart, Subname, Dinplatname, Subtopping


# After login, bring every objects into index.html. When user having current=False Cart, create current=True cart.
@login_required
def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    context = {
        "user": request.user,
        "type": Type.objects.all(),
        "size": Size.objects.all(),
        "style": Style.objects.all(),
        "topping": Topping.objects.all(),
        "subname": Subname.objects.all(),
        "subtopping": Subtopping.objects.all(),
        "saladpasta": SaladPasta.objects.all(),
        "dinplatname": Dinplatname.objects.all(),
    }
    Cart.objects.get_or_create(user=request.user, current=True)

    return render(request, "index.html", context)

# When user submit Add button of the pizza selector, it creates new pizza with every attributes.
def addpizza(request):
    usercart = Cart.objects.get(user=request.user, current=True)
    style_id = int(request.POST["pizzastyle"])
    type_id = int(request.POST["pizzatype"])
    size_id = int(request.POST["pizzasize"])

# If the selection is regular pizza,
    if style_id == 1:
        if size_id == 1:
            if type_id == 1:
                price = 12.20
            elif type_id == 2:
                price = 13.20
            elif type_id == 3:
                price = 14.70
            elif type_id == 4:
                price = 15.70
            else:
                price = 17.25
        else:
            if type_id == 1:
                price = 17.45
            elif type_id == 2:
                price = 19.45
            elif type_id == 3:
                price = 21.45
            elif type_id == 4:
                price = 23.45
            else:
                price = 25.45
# Else the selection is Sicilian pizza,
    else:
        if size_id == 1:
            if type_id == 1:
                price = 23.45
            elif type_id == 2:
                price = 25.45
            elif type_id == 3:
                price = 27.45
            elif type_id == 4:
                price = 28.45
            else:
                price = 29.45
        else:
            if type_id == 1:
                price = 37.70
            elif type_id == 2:
                price = 39.70
            elif type_id == 3:
                price = 41.70
            elif type_id == 4:
                price = 43.70
            else:
                price = 44.70

# Create pizza object.
    pizza = Pizza.objects.create(style_id=style_id, type_id=type_id, size_id=size_id, price=price)

# If the selection is 1 Topping Pizza,
    if type_id == 2:
        top1_id = int(request.POST["topping1"])
        topping1 = Topping.objects.get(pk = top1_id)
        pizza.topping.add(topping1)
# Else if the selection is 2 Toppings Pizza,
    elif type_id == 3:
        top1_id = int(request.POST["topping1"])
        topping1 = Topping.objects.get(pk = top1_id)
        pizza.topping.add(topping1)
        top2_id = int(request.POST["topping2"])
        topping2 = Topping.objects.get(pk = top2_id)
        pizza.topping.add(topping2)
# Else if the selection is 3 Toppings Pizza,
    elif type_id == 4:
        top1_id = int(request.POST["topping1"])
        topping1 = Topping.objects.get(pk = top1_id)
        pizza.topping.add(topping1)
        top2_id = int(request.POST["topping2"])
        topping2 = Topping.objects.get(pk = top2_id)
        pizza.topping.add(topping2)
        top3_id = int(request.POST["topping3"])
        topping3 = Topping.objects.get(pk = top3_id)
        pizza.topping.add(topping3)

    pizza.cart.add(usercart)

    return HttpResponseRedirect(reverse("index"))

# Add sub menu, with the same method with addpizza.
def addsub(request):
    usercart = Cart.objects.get(user=request.user, current=True)

    subname_id = int(request.POST["subname"])
    size_id = int(request.POST["subsize"])

# Categorized into same prices.
    if subname_id <= 5 or subname_id == 8 or subname_id == 9:
        if size_id == 1:
            price = 6.50
        else:
            price = 7.95
    elif subname_id == 6 or subname_id == 7:
        if size_id == 1:
            price = 7.50
        else:
            price = 8.50
    elif subname_id == 10 or subname_id == 11:
        if size_id == 1:
            price = 6.95
        else:
            price = 8.50
    elif subname_id == 12:
        if size_id == 1:
            price = 4.60
        else:
            price = 6.95
    elif subname_id == 13:
        if size_id == 1:
            price = 5.10
        else:
            price = 7.45
    else:
        if size_id == 1:
            price = 6.95
        else:
            price = 8.50

    sub = Sub.objects.create(name_id=subname_id, size_id=size_id, price=price)
    sub.cart.add(usercart)
# Add topping and $0.50 if topping is selected.
    top_id = int(request.POST["subtopping"])
    topping = Subtopping.objects.get(pk = top_id)
    sub.topping.add(topping)

    if top_id > 1:
        Sub.objects.filter(pk=sub.id).update(price=(price+0.50))

    return HttpResponseRedirect(reverse("index"))

# Salad & Pasta menu are only seven with no option.
def addsaladpasta(request):
    usercart = Cart.objects.get(user=request.user, current=True)
    saladpasta_id = int(request.POST["saladpasta"])
    newsaladpastaorder = SaladPasta.objects.get(pk = saladpasta_id)
    newsaladpastaorder.cart.add(usercart)

    return HttpResponseRedirect(reverse("index"))

# Also same method.
def adddinplat(request):
    usercart = Cart.objects.get(user=request.user, current=True)
    dinplatname_id = int(request.POST["dinplat"])
    size_id = int(request.POST["dinplatsize"])

    if size_id == 1:
        if dinplatname_id == (1 or 4):
            price = 35.00
        elif dinplatname_id == (2 or 3 or 5 or 6) :
            price = 45.00

    else:
        if dinplatname_id == (1 or 4):
            price = 60.00
        elif dinplatname_id == (2 or 3 or 5):
            price = 70.00
        else:
            price = 80.00

    dinplat = Dinplat.objects.create(name_id= dinplatname_id, size_id=size_id, price=price)
    dinplat.cart.add(usercart)
    return HttpResponseRedirect(reverse("index"))

# Reference: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# When user click the Cart link, it shows what are in the current=True cart, and shows the total price.
def user_cart(request, user):
    usercart = Cart.objects.get(user=request.user, current=True)

    pizza = Pizza.objects.filter(cart=usercart)
    sub = Sub.objects.filter(cart=usercart)
    saladpasta = SaladPasta.objects.filter(cart=usercart)
    dinplat = Dinplat.objects.filter(cart=usercart)

    pizza_sum = Pizza.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if pizza_sum == None:
        pizza_sum = 0
    sub_sum = Sub.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if sub_sum == None:
        sub_sum = 0
    saladpasta_sum = SaladPasta.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if saladpasta_sum == None:
        saladpasta_sum = 0
    dinplat_sum = Dinplat.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if dinplat_sum == None:
        dinplat_sum = 0

    total_sum = pizza_sum + sub_sum + saladpasta_sum + dinplat_sum

    context = {
       "cart": usercart,
       "pizza": pizza,
       "sub": sub,
       "saladpasta": saladpasta,
       "dinplat": dinplat,
       "pizza_sum" : pizza_sum,
       "sub_sum": sub_sum,
       "saladpasta_sum": saladpasta_sum,
       "dinplat_sum": dinplat_sum,
       "total_sum": total_sum,
    }
    return render(request, "cart.html", context)

# It removes all of the list in the cart.
def clear(request):
    cartuser = request.user
    usercart = Cart.objects.get(user=cartuser, current=True)

    pizzaorder = Pizza.objects.filter(cart=usercart)
    suborder = Sub.objects.filter(cart=usercart)
    saladorder = SaladPasta.objects.filter(cart=usercart)
    dinplatorder = Dinplat.objects.filter(cart=usercart)

    pizza_sum = Pizza.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if pizza_sum == None:
        pizza_sum = 0
    sub_sum = Sub.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if sub_sum == None:
        sub_sum = 0
    saladpasta_sum = SaladPasta.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if saladpasta_sum == None:
        saladpasta_sum = 0
    dinplat_sum = Dinplat.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if dinplat_sum == None:
        dinplat_sum = 0

    total_sum = pizza_sum + sub_sum + saladpasta_sum + dinplat_sum
# If there is nothing in the cart, returns error message.
    if total_sum == 0:
        return render(request, "error.html", {"message": "Nothing in your cart."})
    else:
        for item in pizzaorder:
            item.cart.remove(usercart)
        for item in suborder:
            item.cart.remove(usercart)
        for item in saladorder:
            item.cart.remove(usercart)
        for item in dinplatorder:
            item.cart.remove(usercart)

    context = {
        "message": 'Cart is Cleared.'
    }
    return render(request, "success.html", context)

# Order button gives nothing but changes current=True cart to False, and create new current=True cart, so that the previous cart records remain in the DB.
def order(request):
    cartuser = request.user
    usercart = Cart.objects.get(user=cartuser, current=True)

    pizza_sum = Pizza.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if pizza_sum == None:
        pizza_sum = 0
    sub_sum = Sub.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if sub_sum == None:
        sub_sum = 0
    saladpasta_sum = SaladPasta.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if saladpasta_sum == None:
        saladpasta_sum = 0
    dinplat_sum = Dinplat.objects.filter(cart=usercart).aggregate(Sum('price'))['price__sum']
    if dinplat_sum == None:
        dinplat_sum = 0

    total_sum = pizza_sum + sub_sum + saladpasta_sum + dinplat_sum

    if total_sum == 0:
        return render(request, "error.html", {"message": "Nothing in your cart."})
    else:
        usercart.current = False
        usercart.save()
        Cart.objects.create(user=request.user, current=True)
        context = {
            "message": "Order is completed. We already know where you are and your card numbers, so don't worry!"
        }
        return render(request, "success.html", context)

# [Personal Touch] Retrieve previous order list from DB.
def user_orders(request, user):
    cartuser = request.user
    usercart = Cart.objects.filter(user=cartuser, current=False)

    context = {
        'cartuser': cartuser,
        'usercart': usercart,
    }
    return render(request, "orders.html", context)

# [Person Touch] Each list of the previous order list.
def previousorders(request, cart_id):

    cart = Cart.objects.get(pk=cart_id)

    pizzaorder = Pizza.objects.filter(cart=cart)
    suborder = Sub.objects.filter(cart=cart)
    saladpastaorder = SaladPasta.objects.filter(cart=cart)
    dinplatorder = Dinplat.objects.filter(cart=cart)

    context = {
        'cart': cart,
        'pizzaorder': pizzaorder,
        'suborder': suborder,
        'saladpastaorder': saladpastaorder,
        'dinplatorder': dinplatorder,
        'user': request.user,
    }
    return render(request, "previousorder.html", context)