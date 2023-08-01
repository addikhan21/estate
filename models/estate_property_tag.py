from odoo import fields, models


class estatepropertytag(models.Model):
    _name = "estateproperty.tag"
    _description = "Model for Real-Estate Properties tag"

    name=fields.Char(required=True)