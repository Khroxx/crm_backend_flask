from . import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    role = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Admin {self.username}"

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    phone = db.Column(db.String(20))
    position = db.Column(db.String(100), nullable=True) #Position in company

    def __repr__(self):
        return f"Angestellter {self.first_name} {self.last_name}"

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    phone = db.Column(db.String(20))

    def __repr__(self):
        return f"Kunde, {self.first_name} {self.last_name}"

class Project(db.Model): #OpenSource projects
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Projekt {self.name}, id: {self.id}"

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #members = db.Column(

