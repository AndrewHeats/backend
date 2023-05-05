from db import db


class CoordinateModel(db.Model):
    __tablename__ = "coordinates"

    id = db.Column(db.Integer, primary_key=True)
    l = db.Column(db.Float(precision=2), nullable=False)
    w = db.Column(db.Float(precision=2), nullable=False)
    h = db.Column(db.Float(precision=2), nullable=False)
    time = db.Column(db.Integer, nullable=True)

    field = db.relationship("FieldModel", back_populates="coordinates")
    field_id = db.Column(
        db.Integer, db.ForeignKey("fields.id"), unique=False, nullable=False
    )
