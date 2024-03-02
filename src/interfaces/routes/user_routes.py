# app/interfaces/routes/user_routes.py
from flask import jsonify, request
from src import app
from src.application.user_service import UserService

@app.route('/users', methods=['POST'])
def create_user():
    
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if not name or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400
    new_user, error = UserService.create_user(name, email, password)
    if new_user:
        return jsonify(new_user.as_dict()), 201
    else:
        return jsonify({'message': error}), 400
