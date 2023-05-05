from db import db


class CoordinateModel(db.Model):
    __tablename__ = "coordinates"

    id = db.Column(db.Integer, primary_key=True)
    lon = db.Column(db.Integer, nullable=False)
    wid = db.Column(db.Integer, nullable=False)
    high = db.Column(db.Integer, nullable=False)
    tim = db.Column(db.Integer, nullable=False)

    '''field = db.relationship("FieldModel", back_populates="coordinates")
    field_id = db.Column(
        db.Integer, db.ForeignKey("fields.id"), unique=False, nullable=False
    )
    vehicle = db.relationship("VehicleModel", back_populates="coordinates")

    vehicle_id = db.Column(
        db.Integer, db.ForeignKey("vehicles.id"), unique=False, nullable=False
    )'''
