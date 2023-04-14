from datetime import datetime, timedelta
from project.models import Secret


def test_new_secret():
    """
    GIVEN a Secret model
    WHEN a new Secret is created
    # THEN check the email, hashed_password, and role fields are defined correctly
    """
    secret = Secret(name="secret_name",
               key='abc123',
               value="test_secret",
               password="test_password",
               views_remaining=1,
               created_at=datetime.now(),
               expires_at=datetime.now() + (timedelta(hours=1)))
    assert secret.name == "secret_name"
    assert secret.__repr__() == "<Secret secret_name>"
    # assert secret.hashed_password != 'FlaskIsAwesome'
    # assert secret.role == 'user'