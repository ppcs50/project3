# Project 3

Web Programming with Python and JavaScript


## 1. a short write-up
This is a web food ordering system designed for Pinocchio's Pizza & Subs. A user can order whatever they want, from the various selections of the restaurant.


## 2. file description

### /orders
#### views.py
This is the main file which includes all of the functions. Please see the comments I had put on each of the function.

#### urls.py
This file connects every url and path.

#### forms.py
This is a file for user login and signin function(reference: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html)

### /templates

#### base.html
The base html file for every other. It includes metadata, link, script, header, and nav.

#### login.html, signup.html
This file also refrenced from simpleisbetterthancomplex.com.

#### index.html
Menu selections and basic information are all in here.

#### cart.html
The list of the menu a user has added.

#### orders.html
The list of the previous order of the user.

#### previousorder.html
The list of the menu of a specific previous order.

#### success.html & error.html
Nothing special.

### /static

#### style.css, background.png
style.css file for webpage, and background.png file refrence from www.postmates.com.

### /migrations


## 3. a comment
[Personal Touch]Any user can check his/her previous order list, and also can retrieve every information in a specific order, such as which menu and how much was it.
[Personal Touch]User also can clear the current cart by clicking the Clear button.