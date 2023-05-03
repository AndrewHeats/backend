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
    long = fields.Float(required=True)
    width = fields.Float(required=True)
    height = fields.Float(required=True)
    time = fields.Float(required=True)


class VehicleSchema(PlainVehicleSchema):
    coordinates = fields.Nested(PlainCoordinateSchema(), dump_only=True)


class FieldSchema(PlainFieldSchema):
    coordinates = fields.Nested(PlainCoordinateSchema(), dump_only=True)


class CoordinateFieldSchema(PlainCoordinateSchema):
    field_id = fields.Int(required=True)
    field = fields.Nested(PlainFieldSchema(), dump_only=True)


class CoordinateVehicleSchema(PlainCoordinateSchema):
    vehicle_id = fields.Int(required=True)
    vehicle = fields.Nested(PlainVehicleSchema(), dump_only=True)


class VehicleUpdateSchema(Schema):
    name_of_owner = fields.Str()
    type = fields.Str(required=True)


class FieldUpdateSchema(Schema):
    area = fields.Float()
    plant = fields.Str(required=True)
    process = fields.Str(required=True)
