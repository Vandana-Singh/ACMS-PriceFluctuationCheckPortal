"""
    Manually updating the Price of a particular Product to Test working of Notification system.

"""
from flask import Blueprint
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from .models import db, Product
from sqlalchemy import update

mock = Blueprint('mock', __name__)

@mock.route('/update/<int:product_pid>/<int:product_price>', methods = ['POST' , 'GET'])
@login_required
def update_price(product_pid,product_price):
    """ Updtaing the price of Product  - Permission (Admin Only)"""
    
    if(current_user.email == "admin@acms.com" and check_password_hash(current_user.password, "acms") ):
        
        prod = Product.query.filter_by(pid = product_pid).update(dict(price=product_price))
        db.session.commit()
        prod = Product.query.filter_by(pid = product_pid).first()
        
        if prod.price != product_price:    
            return "Error! Product Price could not be Updated"
        else:
            return True
    else: 
        return "Admin is only allowed to update price"