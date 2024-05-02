from flask import Blueprint, request, jsonify
from app.models.student import Student, db
import validators
# from email_validator import validate_email, EmailNotValidError

student = Blueprint('student', __name__, url_prefix='/api/v1/student')

@student.route('/register', methods=["POST"])
def register():
    try:
        data = request.json
        required_fields = ["first_name", "last_name", "email"]
        
        if not all(field in data for field in required_fields):
            return jsonify({'error': "All fields are required"}), 400
        
        if Student.query.filter_by(email=data["email"]).first():
            return jsonify({'error': "The email already exists"}), 400
        
        new_student = student(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            
            
        )
        
        db.session.add(new_student)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@student.route('/students/<int:student_id>', methods=["GET"])
def get_student(student_id):
    try:
        student = student.query.get(student_id)
        
        if not student:
            return jsonify({'error': 'User not found'}), 404
        
        serialized_student = {
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'email': student.email,
            
        }
        
        return jsonify({'user': serialized_student}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@student.route('/update/<int:student_id>', methods=["PUT"])
def edit_user(student_id):
    try:
        data = request.json
        student = Student.query.get(student_id)

        if not student:
            return jsonify({'error': 'User not found'}), 404

        for field in ["first_name", "last_name", "email"]:
            if field in data:
                setattr(student, field, data[field])
        db.session.commit()

        return jsonify({'message': 'Student updated successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

