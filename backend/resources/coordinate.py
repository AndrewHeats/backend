from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import CoordinateModel
from schemas import CoordinateSchema, CoordinateUpdateSchema

blp = Blueprint("Coordinates", "coordinates", description="Operation on coordinates")


@blp.route("/coordinate/<int:coordinate_id>")
class Coordinate(MethodView):
    @blp.response(200, CoordinateSchema)
    def get(self, coordinate_id):
        coordinate = CoordinateModel.query.get_or_404(coordinate_id)
        return coordinate

    def delete(self, coordinate_id):
        coordinate = CoordinateModel.query.get_or_404(coordinate_id)
        db.session.delete(coordinate)
        db.session.commit()
        db.session.close()
        return {"message": "Coordinates deleted succesfully"}

    @blp.arguments(CoordinateUpdateSchema)
    @blp.response(200, CoordinateSchema)
    def put(self, coordinate_data, coordinate_id):
        coordinate = CoordinateModel.query.get(coordinate_id)

        if coordinate:
            coordinate.high = coordinate_data["high"]
            coordinate.wid = coordinate_data["wid"]
            coordinate.lon = coordinate_data["lon"]
            coordinate.tim = coordinate_data["tim"]
        else:
            coordinate = CoordinateModel(**coordinate_data)

        db.session.add(coordinate)
        db.session.commit()
        db.session.close()
        return coordinate


@blp.route("/coordinates")
class CoordinatesList(MethodView):
    @blp.arguments(CoordinateSchema)
    @blp.response(201, CoordinateSchema)
    def post(self, coordinate_data):
        coordinate = CoordinateSchema(**coordinate_data)

        try:
            db.session.add(coordinate)
            db.session.commit()
            db.session.close()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return coordinate
