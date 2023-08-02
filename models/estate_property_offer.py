from odoo import fields, models


class estatepropertyoffer(models.Model):
    _name = "estateproperty.offer"
    _description = "Model for Real-Estate Properties offer"

    offer_price = fields.Float()
    status_SELECTION = [
        ('accepted', 'Accepted'),
        ('refused', 'Refused '),
    ]
    status = fields.Selection(status_SELECTION, string="status", default='Accepted', Copy=False)
    partner_id = fields.Many2one("estate.property", string="partner", required=True)
