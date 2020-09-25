# -*- coding: utf-8 -*-
#########################################################
from datetime import datetime

from app import db
from app.exceptions import InternalServerError


class BaseModel(db.Model):
    __abstract__ = True

    create_date = db.Column(db.DateTime, default=db.func.now())
    update_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise InternalServerError(e)

    def save(self):
        try:
            self.update_date = datetime.now()
            db.session.add(self)
            db.session.flush()
            db.session.commit()
            return self
        except Exception as e:
            print(e)
            db.session.rollback()
            raise InternalServerError(e)

