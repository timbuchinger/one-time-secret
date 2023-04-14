import datetime
import pytest

from project import create_app, db
from project.models import Secret


@pytest.fixture(scope='module')
def test_client():

    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()
    first = Secret(name='test',
                       key='abc123',
                       value='secret value goes here',
                       password='Password..1',
                       views_remaining='5',
                       created_at=datetime.now(),
                       expires_at=datetime.now() + (datetime.timedelta(hours=1)))

    db.session.add(first)
    db.session.commit()

    yield

    db.drop_all()


@pytest.fixture(scope='module')
def cli_test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    runner = flask_app.test_cli_runner()

    yield runner
