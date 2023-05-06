from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import FieldModel
from schemas import PlainFieldSchema, FieldUpdateSchema

blp = Blueprint("Fields", "fields", description="Operation on fields")


@blp.route("/field/<string:field_id>")
class Field(MethodView):
    @blp.response(200, PlainFieldSchema)
    def get(self, field_id):
        field = FieldModel.query.get_or_404(field_id)
        return field

    def delete(self, field_id):
        field = FieldModel.query.get_or_404(field_id)
        db.session.delete(field)
        db.session.commit()
        db.session.close()
        return {"message": "Field deleted"}, 200

    @blp.arguments(FieldUpdateSchema)
    @blp.response(200, PlainFieldSchema)
    def put(self, field_data, field_id):
        field = FieldModel.query.get(field_id)

        if field:
            field.area = field_data["area"]
            field.plant = field_data["plant"]
            field.process = field_data["process"]
        else:
            field = FieldModel(id=field_id, **field_data)

        db.session.add(field)
        db.session.commit()
        db.session.close()
        return field


@blp.route("/field")
class FieldList(MethodView):
    @blp.response(200, PlainFieldSchema(many=True))
    def get(self):
        return FieldModel.query.all()

    @blp.arguments(PlainFieldSchema)
    @blp.response(201, PlainFieldSchema)
    def post(self, field_data):
        field = FieldModel(**field_data)

        try:
            db.session.add(field)
            db.session.commit()
            db.session.close()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return field
