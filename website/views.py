from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import login_required, current_user
from .models import User, Address
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'POST':
        address = request.form.get('address')
        state = request.form.get('state')
        zip_code = request.form.get('zip_code')

        new_address = Address(address=address,state=state,zip_code=int(zip_code), user_id=current_user.id)
        db.session.add(new_address)
        db.session.commit()
        flash('Address added!', category='success')
        return redirect(url_for('views.home'))

    return render_template("location.html", user=current_user)