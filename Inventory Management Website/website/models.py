from . import db
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import DateTime

class User(db.Model,UserMixin):
    
    phone=db.Column(db.Integer,primary_key=True)
    address=db.Column(db.String(150))
    password =db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    def get_id(self):
        return str(self.phone)
class Product(db.Model):
    product_id=db.Column(db.Integer,primary_key=True)
    product_name=db.Column(db.String(200))
    product_price=db.Column(db.Integer)
    quantity_available = db.Column(db.Integer)
    image_url = db.Column(db.String(255))


class Cart(db.Model):
    cart_id = db.Column(db.Integer, db.ForeignKey('user.phone'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    order_customer=db.Column(db.Integer,db.ForeignKey('user.phone'))
    order_date_time=db.Column(db.DateTime, default=datetime.now)
    order_summary=db.Column(db.String(1000))
    order_amount=db.Column(db.Integer)
    address=db.Column(db.String(150),db.ForeignKey('user.address'))





