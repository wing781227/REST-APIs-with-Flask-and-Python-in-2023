# from marshmallow import Schema, fields


# class ItemSchema(Schema):
#     id = fields.Str(dump_only=True)
#     name = fields.Str(required=True)
#     price = fields.Str(required=True)
#     store_id = fields.Str(required=True)

# class ItemUpdateSchema(Schema):
#     name = fields.Str()
#     price = fields.Float()


# class StoreSchema(Schema):
#     id = fields.Str(dump_only=True)
#     name = fields.Str(required=True)

from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Str(required=True)

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(Schema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)