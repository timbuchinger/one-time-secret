import random
import string
from datetime import datetime, timedelta
from operator import or_

import sqlalchemy

from flask import current_app, render_template, request
from project.models import Secret, db

from . import secrets_blueprint


@secrets_blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@secrets_blueprint.route('/')
@secrets_blueprint.route('/index')
def index():
    return render_template('index.html')


@secrets_blueprint.route('/list')
def list_secrets():
    secrets = Secret.query.all()
    return render_template('list.html', secrets=secrets)


@secrets_blueprint.route('/view/<key>')
def view_secret(key):
    try:
        secret = Secret.query.filter(
            Secret.key == key, Secret.views_remaining > 0, Secret.expires_at > datetime.now()).one()
        secret.views_remaining -= 1
        db.session.commit()
        return render_template('view.html', secret=secret)
    except sqlalchemy.orm.exc.NoResultFound:
        current_app.logger.error('No secret found with key %s', key)
        return render_template('error.html')
    except Exception as e:
        current_app.logger.error('Unexpected error: %s', str(e))
        return render_template('error.html')


@secrets_blueprint.route('/create', methods=['POST'])
def create_secret():
    secret = Secret(name=request.form['name'],
                    key=''.join(random.choice(string.ascii_lowercase)
                                for i in range(20)),
                    value=request.form['secret'].encode(),
                    password=request.form['password'],
                    views_remaining=request.form['views_remaining'],
                    created_at=datetime.now(),
                    expires_at=datetime.now() + (timedelta(hours=1)))

    db.session.add(secret)
    db.session.commit()
    db.session.refresh(secret)

    return render_template('create.html', key=secret.key)


@secrets_blueprint.route('/cleanup', methods=['DELETE'])
def delete_expired_secrets():
    secrets = Secret.query.filter(
        or_(Secret.views_remaining > 0, Secret.expires_at > datetime.now())).all()
    for secret in secrets:
        db.session.delete(secret)
    db.session.commit()
    return "", 204
