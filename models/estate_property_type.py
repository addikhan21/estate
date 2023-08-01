from odoo import fields, models


class estatepropertytype(models.Model):
    _name = "estateproperty.type"
    _description = "Model for Real-Estate.Property.type"
    _rec_name = 'name'

    my_new_house = fields.Char()
    name=fields.Char()
    Title = fields.Char()
    postcode = fields.Char()
    bedrooms = fields.Integer()
    expected_price = fields.Float()
    selling_price = fields.Float()
    living_area_SQM = fields.Integer()