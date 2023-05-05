from db import db


class VehicleModel(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    name_of_owner = db.Column(db.String(100), nullable=False, unique=False)
    type = db.Column(db.String, nullable=False)

    field = db.relationship("FieldModel", back_populates="vehicles")
    field_id = db.Column(
        db.Integer, db.ForeignKey("fields.id"), unique=False, nullable=False
    )
