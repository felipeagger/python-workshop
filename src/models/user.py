from datetime import datetime
from sqlalchemy import Column, DateTime

from src.models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    birth_date = db.Column(db.String(10))
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())

    def get_as_dict(self):
        person = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birth_date': self.birth_date
        }
        return person
