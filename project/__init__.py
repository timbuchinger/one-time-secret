import os
import sqlalchemy as sa
from click import echo
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler


db = SQLAlchemy()

def create_app(config_filename=None):
    app = Flask(__name__)

    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)

    initialize_extensions(app)
    register_blueprints(app)
    # configure_logging(app)
    register_cli_commands(app)

    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    if not inspector.has_table("secret"):
        with app.app_context():
            db.drop_all()
            db.create_all()
            app.logger.info('Initialized the database!')
    else:
        app.logger.info('Database already contains the secret table.')

    return app


def initialize_extensions(app):
    db.init_app(app)

    from project.secrets.cron import cleanup_job
    sched = APScheduler()
    sched.init_app(app)
    sched.api_enabled = True
    sched.add_job(func=cleanup_job, id="do_cleanup_job", trigger='interval', seconds=30)
    sched.start()


def register_blueprints(app):
    from project.secrets import secrets_blueprint
    app.register_blueprint(secrets_blueprint)


def register_cli_commands(app):
    @app.cli.command('init_db')
    def initialize_database():
        """Initialize the database."""
        db.drop_all()
        db.create_all()
        echo('Initialized the database!')
