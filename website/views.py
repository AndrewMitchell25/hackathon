from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import login_required, current_user, login_user
from .models import User, Address
from . import db
from website.house import OnlyFunctionYouNeed

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/about')
def about():
    return render_template("about.html", user=current_user)

@views.route('/consultation')
def consultation():
    if(not current_user.is_authenticated):
        return redirect(url_for('auth.sign_up'))
    address = Address.query.get(int(current_user.id))
    if(not address):
        return redirect(url_for('views.location'))
    price = OnlyFunctionYouNeed(address.zip_code, address.panels, address.meb, address.county, address.state)
    return render_template("consultation.html", user=current_user, price=price)

@views.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'POST':
        old_address = Address.query.get(int(current_user.id))
        if old_address:
            db.session.delete(old_address)
            db.session.commit()

        address = request.form.get('address')
        county = request.form.get('county')
        state = request.form.get('state')
        zip_code = request.form.get('zip_code')
        meb = request.form.get('meb')
        panels = request.form.get('panels')

        new_address = Address(address=address, county=county, state=state, zip_code=int(
            zip_code), meb=int(meb), panels=int(panels), user_id=current_user.id)
        db.session.add(new_address)
        db.session.commit()
        flash('Address added!', category='success')
        return redirect(url_for('views.consultation'))

    return render_template("location.html", user=current_user)
