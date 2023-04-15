import os
from sqlalchemy import func
from project import db
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine


class Secret(db.Model):
    # key = 'test'
    key = os.environ.get("ENCRYPTION_KEY", default='BAD_SECRET_KEY')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    key = db.Column(db.String(100), nullable=False)
    value = db.Column(EncryptedType(db.String, length=255, key=key), nullable=False)
    password = db.Column(db.String(100))
    views_remaining = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                            server_default=func.now())
    expires_at = db.Column(db.DateTime(timezone=True))

    def __repr__(self):
        return f'<Secret {self.name}>'
