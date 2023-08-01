from odoo import api, fields, models

class TestComputed(models.Model):
    _name = "estateproperty.testcompute"

    total = fields.Float(compute="_compute_total",inverse="_inverse_total")
    amount = fields.Float()

    @api.depends("amount")
    def _compute_total(self):
        for record in self:
            record.total = 2.0 * record.amount
            print(record.total)