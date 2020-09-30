# -*- coding: utf-8 -*-
#########################################################
from app import db
from app.models import BaseModel


class Example(BaseModel):
    __tablename__ = "example"

    exampleId = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), default="", nullable=False)










