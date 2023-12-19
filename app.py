from flask import Flask, jsonify, request, render_template,url_for,redirect,flash
from flask_cors import cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from waitress import serve


db = SQLAlchemy()
app = Flask(__name__)

    # Your app configuration and routes go here
    # Database Name
db_name = 'yoga.db'

# Configuring SQLite Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

# Suppresses warning while tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialising SQLAlchemy with Flask App
db.init_app(app)

#Definign tables in databases: 
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    enrollments = db.relationship('Enrollment', backref='user', lazy=True)

class Batch(db.Model):
    batch_id = db.Column(db.Integer, primary_key=True)
    timeslot = db.Column(db.String(20), nullable=False)
    enrollments = db.relationship('Enrollment', backref='batch', lazy=True)

class Enrollment(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.batch_id'), nullable=False)
    enrolled_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    payments = db.relationship('Payment', backref='enrollment', lazy=True)

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollment.enrollment_id'), nullable=False)
    paid_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

batch_values = [
    { 'timeslot': '6-7AM'},
    { 'timeslot': '7-8AM'},
    { 'timeslot': '8-9AM'},
    { 'timeslot': '5-6PM'}
]


with app.app_context():
    db.create_all()
    for value in batch_values:
        timeslot = value['timeslot']
        existing_batch = Batch.query.filter_by(timeslot=timeslot).first()
        if not existing_batch:
            batch = Batch(timeslot=timeslot)
            db.session.add(batch)

    db.session.commit()


# Define your routes and endpoints here
@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    
    error_messages = {}
    if request.method == 'POST':
        # Handle form submission
        data = request.form.to_dict() 
        print(data)

        user = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        batch_timeslot = request.form.get('timeslot')

        # Validate username
        if not user or len(user.strip()) == 0:
            error_messages['name'] = 'Username is required.'

        # Validate email
        if not email or len(email.strip()) == 0:
            error_messages['email'] = 'Email is required.'
        elif '@' not in email or '.' not in email:
            error_messages['email'] = 'Provide a valid email.'

        # Validate age
        try:
            age = int(age)
            if age < 18 or age > 65:
                error_messages['age'] = 'Age must be between 18 and 65.'
        except ValueError:
            error_messages['age'] = 'Invalid age.'

        # Validate batch
        if not batch_timeslot or len(batch_timeslot.strip()) == 0:
            error_messages['timeslot'] = 'Select a valid batch.'

        if error_messages:
            return render_template('register.html', error_messages=error_messages)

        # Create a new user instance
        new_user = User(user=user, email=email, age=age)
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            error_messages['exists']="User is registered. Visit renew page for next month renewal"
        else:
            db.session.add(new_user)
            db.session.commit()

            # Get the user_id of the newly created user
            user_id = new_user.user_id
            # Query the Batch table to get the batch_id based on timeslot
            
            batch = Batch.query.filter_by(timeslot=batch_timeslot).first()
            # Create a new enrollment instance
            new_enrollment = Enrollment(user_id=user_id, batch_id=batch.batch_id)

            # Add the new enrollment to the database
            db.session.add(new_enrollment)
            db.session.commit()

        return redirect(url_for("user",usr=user))

    # Render the registration form
    return render_template('register.html', error_messages=error_messages)


# Example endpoint for handling POST requests
@app.route('/<usr>')
def user(usr):
    return f"<h1>Successfully registered ,{usr} !</h1>"
    # return render_template('confirmation.html')


@app.route('/changeSchedule.html', methods=['GET', 'POST'])
def change_schedule():
    error_messages = {}
    if request.method == 'POST':
        # Handle form submission
        data = request.form.to_dict() 
        print(data)
        user ="Sucess"

        
        email = request.form.get('email')
        batch_timeslot = request.form.get('timeslot')

        # Validate email
        if not email or len(email.strip()) == 0:
            error_messages['email'] = 'Email is required.'
        elif '@' not in email or '.' not in email:
            error_messages['email'] = 'Provide a valid email.'

        # Validate batch
        if not batch_timeslot or len(batch_timeslot.strip()) == 0:
            error_messages['timeslot'] = 'Select a valid batch.'

        if error_messages:
            return render_template('changeSchedule.html', error_messages=error_messages)

        # Retrieve the existing user
        existing_user = User.query.filter_by(email=email).first()

        if not existing_user:
            error_messages['exists'] = "User not registered. Register first"
            # return render_template('changeSchedule.html', error_messages=error_messages)
        # Retrieve the existing enrollment for the user
        existing_enrollment = Enrollment.query.filter_by(user_id=existing_user.user_id).first()

        # Update the timeslot of the existing enrollment
        existing_enrollment.batch_id = Batch.query.filter_by(timeslot=batch_timeslot).first().batch_id
        db.session.commit()
        
        return redirect(url_for("user",usr=user))

    return render_template('changeSchedule.html', error_messages=error_messages)

@app.route('/payment.html', methods=['GET','POST'])
def payment():
    error_messages = {}
    if request.method == 'POST':
        # Handle payment form submission
        # Retrieve data from the form
        email = request.form.get('email')
        
        payment_status = True  # Set to True if payment is successful Mock function
        # Validate email
        if not email or len(email.strip()) == 0:
            error_messages['email'] = 'Email is required.'
        elif '@' not in email or '.' not in email:
            error_messages['email'] = 'Provide a valid email.'

        if error_messages:
            return render_template('payment.html', error_messages=error_messages)
        
        # Retrieve the existing user
        existing_user = User.query.filter_by(email=email).first()

        if not existing_user:
            error_messages['exists'] = "You are not enrolled. Please register first"
        
        # Retrieve the existing enrollment for the user
        existing_enrollment = Enrollment.query.filter_by(user_id=existing_user.user_id).first()

        # Create a new payment record
        new_payment = Payment(user_id=existing_user.user_id, enrollment_id=existing_enrollment.enrollment_id)
        db.session.add(new_payment)
        db.session.commit()
        
        # Render the payment confirmation page
        return redirect(url_for("pay",pyy=" :)"))
    return render_template('payment.html', error_messages=error_messages)
# Example endpoint for handling POST requests
@app.route('/<pyy>')
def pay(pyy):
    return f"<h1>Payment Successfull {pyy} !</h1>"
    # return render_template('confirmation.html')



if __name__ == '__main__':
    # Run the app using Waitress when executed directly
    # serve(create_app(), host='0.0.0.0', port=5000)
    app.run(debug=True)
