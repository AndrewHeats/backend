from marshmallow import Schema, fields


class PlainVehicleSchema(Schema):
    id = fields.Int(dump_only=True)
    name_of_owner = fields.Str(required=True)
    type = fields.Str(required=True)


class PlainFieldSchema(Schema):
    id = fields.Int(dump_only=True)
    area = fields.Float(required=True)
    plant = fields.Str(required=True)
    process = fields.Str(required=True)


class PlainCoordinateSchema(Schema):
    id = fields.Int(dump_only=True)
    l = fields.Float(required=True)
    w = fields.Float(required=True)
    h = fields.Float(required=True)
    time = fields.Float(required=True)


class VehicleSchema(PlainVehicleSchema):
    """coordinate_id = fields.Int(required=True)
    coordinates = fields.Nested(PlainCoordinateSchema(), dump_only=True)"""
    field_id = fields.Int(required=True)
    field = fields.Nested(PlainFieldSchema(), dump_only=True)


class FieldSchema(PlainFieldSchema):
    coordinate_id = fields.Int(required=True)
    coordinates = fields.Nested(PlainCoordinateSchema(), dump_only=True)


class CoordinateSchema(PlainCoordinateSchema):
    field_id = fields.Int()
    field = fields.Nested(PlainFieldSchema(), dump_only=True)
    vehicle_id = fields.Int()
    vehicle = fields.Nested(PlainVehicleSchema(), dump_only=True)


class VehicleUpdateSchema(Schema):
    name_of_owner = fields.Str()
    type = fields.Str(required=True)


class FieldUpdateSchema(Schema):
    area = fields.Float(required=True)
    plant = fields.Str(required=True)
    process = fields.Str(required=True)


class CoordinateUpdateSchema(Schema):
    time = fields.Int(required=True)
    l = fields.Float(required=True)
    h = fields.Float(required=True)
    w = fields.Float(required=True)
