from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospitals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Hospital Model
class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    total_beds = db.Column(db.Integer, nullable=False)
    available_beds = db.Column(db.Integer, nullable=False)
    doctors = db.relationship('Doctor', backref='hospital', lazy=True)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

# Doctor Model
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    schedule = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False, default=4.5)
    image_url = db.Column(db.String(200), nullable=False)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)

# Create all tables
with app.app_context():
    db.create_all()
    
    # Add sample hospitals if none exist
    if Hospital.query.count() == 0:
        sample_hospitals = [
            {
                'name': 'Metropolitan Medical Center',
                'location': '123 Main Street, Downtown',
                'total_beds': 500,
                'available_beds': 450
            },
            {
                'name': 'Riverside Regional Hospital',
                'location': '456 River Road, Westside',
                'total_beds': 400,
                'available_beds': 350
            },
            {
                'name': 'Sunrise General Hospital',
                'location': '789 Sunrise Avenue, Eastside',
                'total_beds': 600,
                'available_beds': 500
            },
            {
                'name': 'Parkview Medical Center',
                'location': '321 Park Road, Northside',
                'total_beds': 300,
                'available_beds': 275
            }
        ]
        
        for hospital_data in sample_hospitals:
            hospital = Hospital(**hospital_data)
            db.session.add(hospital)
        
        db.session.commit()

# Serve the main page
@app.route('/')
def index():
    return render_template('doctor.html')

@app.route('/hospitals')
def hospitals():
    return render_template('hospitals.html')

@app.route('/doctors')
def doctors():
    return render_template('doctor.html')  # Using index.html for doctors page since it has the doctors list

# API Routes
@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([{
        'id': d.id,
        'name': d.name,
        'specialization': d.specialization,
        'schedule': d.schedule,
        'rating': d.rating,
        'image': d.image_url
    } for d in doctors])

@app.route('/api/doctors', methods=['POST'])
def add_doctor():
    data = request.json
    doctor = Doctor(
        name=data['name'],
        specialization=data['specialization'],
        schedule=data['schedule'],
        rating=data.get('rating', 4.5),
        image_url=data.get('image_url', 'https://randomuser.me/api/portraits/men/36.jpg'),
        hospital_id=data['hospital_id']
    )
    db.session.add(doctor)
    db.session.commit()
    return jsonify({'message': 'Doctor added successfully', 'id': doctor.id})

@app.route('/api/hospitals', methods=['GET'])
def get_hospitals():
    hospitals = Hospital.query.all()
    return jsonify([{
        'id': h.id,
        'name': h.name,
        'location': h.location,
        'total_beds': h.total_beds,
        'available_beds': h.available_beds,
        'doctors': [{
            'id': d.id,
            'name': d.name,
            'specialization': d.specialization,
            'schedule': d.schedule,
            'rating': d.rating,
            'image': d.image_url
        } for d in h.doctors],
        'last_updated': h.last_updated.isoformat()
    } for h in hospitals])

@app.route('/api/hospitals', methods=['POST'])
def add_hospital():
    data = request.json
    hospital = Hospital(
        name=data['name'],
        location=data['location'],
        total_beds=data['total_beds'],
        available_beds=data['available_beds']
    )
    db.session.add(hospital)
    db.session.commit()
    return jsonify({'message': 'Hospital added successfully', 'id': hospital.id})

if __name__ == '__main__':
    app.run(debug=True, port=5001) 