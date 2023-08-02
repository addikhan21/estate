from odoo import fields, models


class estatepropertytag(models.Model):
    _name = "estateproperty.tag"
    _description = "Model for Real-Estate Properties tag"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    name=fields.Char(required=True)