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


class VehicleSchema(PlainVehicleSchema):
    fields = fields.List(fields.Nested(PlainFieldSchema()), dump_only=True)


class FieldSchema(PlainFieldSchema):
    vehicles = fields.List(fields.Nested(PlainVehicleSchema()), dump_only=True)


class VehicleUpdateSchema(Schema):
    name_of_owner = fields.Str()
    type = fields.Str(required=True)


class FieldUpdateSchema(Schema):
    area = fields.Float()
    plant = fields.Str(required=True)
    process = fields.Str(required=True)


class VehicleAndFieldSchema(Schema):
    message = fields.Str()
    vehicle = fields.Nested(VehicleSchema)
    field = fields.Nested(FieldSchema)
