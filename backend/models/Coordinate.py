from db import db


class CoordinateModel(db.Model):
    __tablename__ = "coordinates"
    long = db.Column(db.Float(precision=2), nullable=False)
    width = db.Column(db.Float(precision=2), nullable=False)
    height = db.Column(db.Float(precision=2), nullable=False)
    time = db.Column(db.Integer, nullable=True)
    field = db.relationship("FieldModel", back_populates="coordinates")
    vehicle = db.relationship("VehicleModel", back_populates="coordinates")

