from odoo import fields, models


class estatepropertytype(models.Model):
    _name = "estateproperty.type"
    _description = "Model for Real-Estate.Property.type"
    _rec_name = 'name'

    name=fields.Char("Name", required=True)