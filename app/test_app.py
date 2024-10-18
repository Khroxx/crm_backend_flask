import pytest
from app import create_app, db
from app.models import AdminUser

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_admin_page(client):
    response = client.get("/adminpanel", follow_redirects=True)
    assert response.status_code == 200
    assert b"Admin" in response.data
    print("adminpanel page passed")

def test_create_admin_user(app):
    with app.app_context():
        admin_user = AdminUser(username="admin", email="admin@example.com")
        db.session.add(admin_user)
        db.session.commit()

        user = AdminUser.query.filter_by(username="admin").first()
        assert user is not None
        assert user.email == "admin@example.com"
    print("adminuser created passed")
    
def test_create_employee(app):
    with app.app_context():
        employee