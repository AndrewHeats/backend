from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError

import db
from models import FieldModel
from schemas import FieldSchema, FieldUpdateSchema

blp = Blueprint("Vehicles", "vehicles", description="Operation on vehicles")


@blp.route("/field/<string:field_id>")
class Vehicle(MethodView):
    @blp.response(200, FieldSchema)
    def get(self, field_id):
        field = FieldModel.query.get_or_404(field_id)
        return field


    def delete(self, field_id):
        field = FieldModel.query.get_or_404(field_id)
        db.session.delete(field)
        db.session.close()
        return {"message": "Field deleted succesfully"}

    @blp.arguments(FieldUpdateSchema)
    @blp.response(200, FieldSchema)
    def put(self, field_data, field_id):
        field = FieldModel.query.get(field_id)

        if field:
            field.area = field_data["area"]
        else:
            field = FieldModel(id=field_id, **field_data)

        db.session.add(field)
        db.session.commit()

        return field




@blp.route("/field")
class FieldList(MethodView):
    @blp.response(200, FieldSchema(many=True))
    def get(self):
        return FieldModel.query.all()

    @blp.arguments(FieldSchema)
    @blp.response(201, FieldSchema)
    def post(self, field_data):
        field = FieldModel(**field_data)

        try:
            db.session.add(field)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return field



