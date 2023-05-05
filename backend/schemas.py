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
    lon = fields.Int(required=True)
    wid = fields.Int(required=True)
    high = fields.Int(required=True)
    tim = fields.Int(required=True)


class VehicleSchema(PlainVehicleSchema):
    coordinate_id = fields.Int(required=True)
    coordinates = fields.Nested(PlainCoordinateSchema(), dump_only=True)


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
    lon = fields.Int(required=True)
    wid = fields.Int(required=True)
    high = fields.Int(required=True)
    tim = fields.Int(required=True)
