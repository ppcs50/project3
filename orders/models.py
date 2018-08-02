from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Size(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"

class Style(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Subname(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Subtopping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Dinplatname(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete='CASCADE')
    current = models.BooleanField()
    date = models.DateField(("Date"), auto_now_add=True)
    time = models.TimeField(("Time"), auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user}'s Cart -- {self.time}_{self.date}"

class Pizza(models.Model):
    style = models.ForeignKey(Style, on_delete = models.CASCADE, related_name="pizzastyle")
    type = models.ForeignKey(Type, on_delete = models.CASCADE, related_name="pizzatype")
    size = models.ForeignKey(Size, on_delete = models.CASCADE, related_name="pizzasize")
    topping = models.ManyToManyField(Topping, blank = True, related_name = "pizzatopping")
    cart = models.ManyToManyField(Cart, blank = True, related_name = "pizza")
    price = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2)

    def __str__(self):
        return f"{self.style}, {self.type}({self.size}): ${self.price}"

class Sub(models.Model):
    name = models.ForeignKey(Subname, on_delete = models.CASCADE, related_name="subname")
    size = models.ForeignKey(Size, null=True, blank=True, on_delete = models.CASCADE, related_name="sub_size")
    topping = models.ManyToManyField(Subtopping, blank = True, related_name = "subtopping")
    cart = models.ManyToManyField(Cart, blank = True, related_name = "sub")
    price = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2)

    def __str__(self):
        return f"{self.name}({self.size}): ${self.price}"

class SaladPasta(models.Model):
    name = models.CharField(max_length=64)
    cart = models.ManyToManyField(Cart, blank = True, related_name = "saladpasta")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name}: ${self.price}"

class Dinplat(models.Model):
    name = models.ForeignKey(Dinplatname, on_delete = models.CASCADE, related_name="dinplatname")
    size = models.ForeignKey(Size, on_delete = models.CASCADE, related_name="dinnerplatter_size")
    cart = models.ManyToManyField(Cart, blank = True, related_name = "dinplat")
    price = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2)

    def __str__(self):
        return f"{self.name}({self.size}): ${self.price}"
