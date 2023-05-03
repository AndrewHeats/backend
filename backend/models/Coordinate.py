from db import db


class CoordinateModel(db.Model):
    __tablename__ = "coordinates"

    id = db.Column(db.Integer, primary_key=True)
    long = db.Column(db.Float(precision=2), nullable=False)
    width = db.Column(db.Float(precision=2), nullable=False)
    height = db.Column(db.Float(precision=2), nullable=False)
    time = db.Column(db.Integer, nullable=True)

    field = db.relationship("FieldModel", back_populates="coordinates")
    field_id = db.Column(
        db.Integer, db.ForeignKey("fields.id"), unique=False, nullable=False
    )
    vehicle = db.relationship("VehicleModel", back_populates="coordinates")
    vehicle_id = db.Column(
        db.Integer, db.ForeignKey("vehicles.id"), unique=False, nullable=False
    )
