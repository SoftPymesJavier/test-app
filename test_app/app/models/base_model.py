# -*- coding: utf-8 -*-
#########################################################
from datetime import datetime

from app import db


class BaseModel(db.Model):
    __abstract__ = True

    create_date = db.Column(db.DateTime, default=db.func.now())
    update_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def delete(self):
        db.session.delete(self)
        db.session.commit()

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
            raise NotImplementedError

