from app import db 
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from app import db  # Separate import
from app.forms import LoginForm

# Create blueprints FIRST
auth_bp = Blueprint('auth', __name__)
main_bp = Blueprint('main', __name__)

# Auth routes
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        graduation_year = request.form.get('graduation_year')
        degree = request.form.get('degree')
        
        hashed_password = generate_password_hash(password)
        new_user = User(
            email=email,
            password=hashed_password,
            name=name,
            graduation_year=graduation_year,
            degree=degree
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.profile'))
        flash('Invalid credentials', 'danger')
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Main routes
@main_bp.route('/')
def home():
    return "Alumni Portal Home Page"

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
