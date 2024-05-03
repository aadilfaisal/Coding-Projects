from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required,current_user
from . import db
import json
from .models import User, Orders,Cart,Product
from sqlalchemy.orm import join



views = Blueprint('views', __name__) 


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        cart_id = current_user.phone  # Assuming phone is the identifier for the user
        
        # Check if the product is already in the cart
        cart_item = Cart.query.filter_by(product_id=product_id).first()
        if cart_item:
            # If the product is already in the cart, increment the quantity
            cart_item.quantity += 1
        else:
            # If the product is new, add it to the cart table
            new_cart_item = Cart(cart_id=cart_id, product_id=product_id, quantity=1)
            db.session.add(new_cart_item)
        
        db.session.commit()
        flash('Product added to cart successfully!', category='success')
        return redirect(url_for('views.home'))

    products = Product.query.all()
    return render_template("index.html", products=products)



@views.route('/cart')
def cart():
    # Fetch all items in the cart for the current user
    cart_items = Cart.query.filter_by(cart_id=current_user.phone).all()
    
    # Fetch product information for each cart item
    cart_with_products = []
    total_cost = 0  # Variable to calculate the total cost of all products in the cart
    
    for item in cart_items:
        product = Product.query.filter_by(product_id=item.product_id).first()
        if product:
            # Calculate the cost of this particular product in the cart
            product_cost = product.product_price * item.quantity
            total_cost += product_cost
            
            # Append the product details along with the quantity and cost to the list
            cart_with_products.append((product, item.quantity, product_cost))
    
    return render_template("cart.html", cart_with_products=cart_with_products, total_cost=total_cost)
    



@views.route('/profile')
@login_required
def profile():
    # Fetch the user's data from the database
    user = current_user
    print("user is : ",user)  # Add this line to print the current_user object
    orders = Orders.query.filter_by(order_customer=user.phone).all()  # Fetch orders associated with the user
    return render_template("profile.html", user=user, orders=orders)

@views.route('/payment')
def payment():
    return render_template("payment.html")
