from db import db


class VehicleModel(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    name_of_owner = db.Column(db.String(100), nullable=False, unique=False)
    type = db.relationship("Type", back_populates="type", lazy="dynamic")
    coordinates = db.relationship("CoordinateModel", back_populates="coordinates", lazy="dynamic")
