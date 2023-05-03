import enum

from marshmallow import Schema, fields

import models.Type


class PlainTypeSchema(Schema):
    type = models.Type.Type(required=True)


class PlainProcessSchema(Schema):
    process = models.Process.Process(required=True)


class PlainPlantSchema(Schema):
    plant = models.Plant.Corn


class PlainVehicleSchema(Schema):
    id = fields.Int(dump_only=True)
    name_of_owner = fields.Str(required=True)


class PlainFieldSchema(Schema):
    id = fields.Int(dump_only=True)
    area = fields.Float(required=True)


class PlainCoordinateSchema(Schema):
    long = fields.Float(required=True)
    width = fields.Float(required=True)
    height = fields.Float(required=True)
    time = fields.Float(required=True)


class VehicleSchema(PlainVehicleSchema):
    coordinates = fields.Nested(PlainCoordinateSchema(), dump_only=True)
    type = fields.Nested(PlainTypeSchema(), dump_only=True)


class FieldSchema(PlainFieldSchema):
    coordinates = fields.Nested(PlainCoordinateSchema(), dump_only=True)
    process = fields.Nested(PlainProcessSchema(), dump_only=True)
    plant = fields.Nested(PlainPlantSchema(), dump_only=True)


class CoordinateSchema(PlainCoordinateSchema):
    field = fields.Nested(PlainFieldSchema(), dump_only=True)
    vehicle = fields.Nested(PlainVehicleSchema(), dump_only=True)


class VehicleUpdateSchema(Schema):
    name_of_owner = fields.Str()


class FieldUpdateSchema(Schema):
    area = fields.Float()
