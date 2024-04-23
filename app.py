from flask import Flask, render_template, request, redirect, url_for ,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/credit_card'
app.config['UPLOAD_FOLDER'] = 'path/to/your/upload/folder'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class SavingsAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)

@app.route('/open_account', methods=['POST'])
def open_account():
    if request.method == 'POST':
        # Parse form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip']

        # Create a new instance of SavingsAccount model
        new_account = SavingsAccount(name=name, email=email, phone=phone, address=address,
                                     city=city, state=state, zip_code=zip_code)

        # Add the new account to the database session
        db.session.add(new_account)
        
        # Commit the transaction
        db.session.commit()

        # Redirect to a success page or home page
        return redirect(url_for('home'))
    
class CheckingAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    
@app.route('/checking_account', methods=['POST'])
def checking_account():
    if request.method == 'POST':
        # Parse form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip']

        # Create a new instance of SavingsAccount model
        new_account = CheckingAccount(name=name, email=email, phone=phone, address=address,
                                     city=city, state=state, zip_code=zip_code)

        # Add the new account to the database session
        db.session.add(new_account)
        
        # Commit the transaction
        db.session.commit()

        # Redirect to a success page or home page
        return redirect(url_for('home'))
    
class BusinessAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100), nullable=False)
    contact_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)

@app.route('/open_business_account', methods=['POST'])
def open_business_account():
    if request.method == 'POST':
        # Parse form data
        business_name = request.form['businessName']
        contact_name = request.form['contactName']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip']

        # Create a new instance of BusinessAccount model
        new_account = BusinessAccount(business_name=business_name, contact_name=contact_name,
                                      email=email, phone=phone, address=address,
                                      city=city, state=state, zip_code=zip_code)

        # Add the new account to the database session
        db.session.add(new_account)
        
        # Commit the transaction
        db.session.commit()

        # Redirect to a success page or home page
        return redirect(url_for('home'))
    
# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services.html')
def services():
    return render_template('services.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/apply.html')
def saving():
    return render_template('apply.html')

@app.route('/apply2.html')
def checking():
    return render_template('apply2.html')

@app.route('/apply4.html')
def business():
    return render_template('apply4.html')

@app.route('/submit_form_message', methods=['POST'])
def submit_form_message():
    if request.method == 'POST':
        message_content = request.form['message']
        new_message = Message(content=message_content)
        db.session.add(new_message)
        db.session.commit()
        return "Message submitted successfully!"
    
    
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(19), nullable=False)
    expiry_date = db.Column(db.String(5), nullable=False)
    cvv = db.Column(db.String(3), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    if request.method == 'POST':
        card_number = request.form['card-number']
        expiry_date = request.form['expiry']
        cvv = request.form['cvv']

        # Create a new Payment object
        new_payment = Payment(card_number=card_number, expiry_date=expiry_date, cvv=cvv)

        # Add the payment to the database session
        db.session.add(new_payment)
        
        # Commit the transaction
        db.session.commit()

        return "Payment processed successfully!"


if __name__ == '__main__':
    with app.app_context():
        # Create all database tables
        db.create_all()
    app.run(debug=True)

       
