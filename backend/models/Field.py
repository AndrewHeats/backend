from db import db


class FieldModel(db.Model):
    __tablename__ = "fields"

    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Float(precision=2), nullable=False)
    process = db.relationship("Process", back_populates="process", lazy="dynamic")
    coordinates = db.relationship("CoordinateModel", back_populates="coordinates", lazy="dynamic")
    plant = db.relationship("Plant", back_populates="plants", lazy="dynamic")
