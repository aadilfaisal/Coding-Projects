from flask import Blueprint, render_template, request, flash, redirect, url_for,get_flashed_messages    
from .models import User , Product 
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user
from flask_login import current_user 
from werkzeug.utils import secure_filename

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')

        if phone == '0123456789' and password == 'admin':
            return redirect(url_for('auth.admin'))

        user = User.query.filter_by(phone=phone).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)  # Log in regular user
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    return redirect(url_for('auth.login'))




@auth.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if request.method == 'POST':
        if 'add-product' in request.form:  # If the add product form is submitted
            product_id = request.form.get('productId')
            product_name = request.form.get('productName')
            product_price = request.form.get('cost')
            quantity_available = request.form.get('quantity')

            # Handle image upload
            if 'productImage' in request.files:
                product_image = request.files['productImage']
                if product_image.filename != '':
                    filename = secure_filename(product_image.filename)
                    product_image.save(f'website/static/images/{filename}')
                    image_url = filename
                else:
                    image_url = None
            else:
                image_url = None

            # Create a new product instance and add it to the database
            new_product = Product(product_id=product_id, product_name=product_name, product_price=product_price,
                                  quantity_available=quantity_available, image_url=image_url)
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!', category='success')
            return redirect(url_for('auth.admin'))

        elif 'remove-product' in request.form:  # If the remove product form is submitted
            product_id = request.form.get('productId')
            product = Product.query.get(product_id)
            if product:
                db.session.delete(product)
                db.session.commit()
                flash('Product removed successfully!', category='success')
            else:
                flash('Product not found!', category='error')
            return redirect(url_for('auth.admin'))

    products = Product.query.all()
    return render_template("admin.html", products=products)



@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        phone = request.form.get('phone')
        address = request.form.get('address')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if first_name is None:
            flash('First name is required.', category='error')
            return redirect(url_for('auth.sign_up'))

        user = User.query.filter_by(phone=phone).first()
        if user:
            flash('Phone number already exists.', category='error')
        elif len(phone) < 10:
            flash('Phone number must be 10 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 5:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(phone=phone, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)


@auth.route('/forgotpassword')
def forgotpassword() :
    return render_template("forgotpassword.html")



