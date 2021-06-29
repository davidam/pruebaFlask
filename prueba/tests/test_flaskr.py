# import os
# import tempfile

# import pytest

# from flaskr import create_app
# from flaskr.db import init_db


# @pytest.fixture
# def client():
#     db_fd, db_path = tempfile.mkstemp()
#     app = create_app({'TESTING': True, 'DATABASE': db_path})

#     with app.test_client() as client:
#         with app.app_context():
#             init_db()
#         yield client

#     os.close(db_fd)
#     os.unlink(db_path)

# def test_empty_db(client):
#     """Start with a blank database."""

#     rv = client.get('/')
#     assert 'Posts' in str(rv.data)


# def login(client, username, password):
#     return client.post('/login', data=dict(
#         username=username,
#         password=password
#     ), follow_redirects=True)

# def logout(client):
#     return client.get('/logout', follow_redirects=True)

# def test_login_logout(client):
#     """Make sure login and logout works."""

#     username = flaskr.app.config["USERNAME"]
#     password = flaskr.app.config["PASSWORD"]

#     rv = login(client, username, password)
#     assert b'You were logged in' in rv.data

#     rv = logout(client)
#     assert b'You were logged out' in rv.data

#     rv = login(client, f"{username}x", password)
#     assert b'Invalid username' in rv.data

#     rv = login(client, username, f'{password}x')
#     assert b'Invalid password' in rv.data
