from flask import Blueprint, request, jsonify, redirect, url_for
from .models import *
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect(url_for('admin.index'))


@main.route('/get/admins', methods=['GET'])
def get_admins():
    admins = AdminUser.query.all()
    return jsonify([{"id": a.id, "username": a.username, "email": a.email,
                     "role": a.role} for a in admins])

@main.route('/admin', methods=['POST'])
def add_admin():
    data = request.get_json()
    new_admin = AdminUser(username=data['username'], email=data['email'],
                      role=data['role'])

    db.session.add(new_admin)
    db.session.commit()

    return jsonify({"message": "Admin added"}), 201



@main.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{"id": e.id, "first_name": e.first_name,
                     "last_name": e.last_name, "email": e.email,
                     "phone": e.phone, "position": e.position} for e in employees])

@main.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(first_name=data['first_name'], last_name=data['last_name'],
                            email=data['email'], phone=data['phone'],
                            position=data['position'])

    db.session.add(new_employee)
    db.session.commit()

    return jsonify({"message": "Employee added"}), 201


@main.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{"id": c.id, "first_name": c.first_name, "last_name": c.last_name,
                     "email": c.email, "phone": c.phone} for c in customers])

@main.route('/customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(first_name=data['first_name'], last_name=data['last_name'],
                            email=data['email'], phone=data['phone'], frontend=data['frontend'],
                            backend=data['backend'])

    db.session.add(new_customer)
    db.session.commit()

    return jsonify({"message": "Customer added"}), 201


@main.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([{"id": p.id, "name": p.name, "text": p.text} for p in projects])

@main.route('/project', methods=['POST'])
def add_project():
    data = request.get_json()
    new_project = Project(name=data['name'], text=data['text'])

    db.session.add(new_project)
    db.session.commit()

    return jsonify({"message": "Project added"})


@main.route('/groups', methods=['GET'])
def get_groups():
    groups = Group.query.all()
    return jsonify([{"id": g.id, "number": g.number} for g in groups])

@main.route('/group', methods=['POST'])
def add_group():
    data = request.get_json()
    new_project = Group(number=data['number'])

    db.session.add(new_project)
    db.session.commit()

    return jsonify({"message": "Group added"}), 201
