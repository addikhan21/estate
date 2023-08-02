from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class EstateProperties(models.Model):
    _name = "estate.property"
    _description = "Model for Real-Estate Properties"
    _rec_name = 'name'

    tag_ids = fields.Integer()
    my_new_house = fields.Char()
    Title = fields.Char()
    name = fields.Char("")
    description = fields.Char("Description")
    Postcode = fields.Char()
    Bedrooms = fields.Integer(default=2)

    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)
    date_availability = fields.Date("Available From", default=lambda self: self._default_date_availability(),
                                    copy=False)
    expected_price = fields.Float("Expected Price")
    selling_price = fields.Float("Selling Price", copy=False)
    living_area_SQM = fields.Integer("Living Area (SQM)")
    available_form = fields.Date("Available Form")
    Facades = fields.Integer()
    Garage = fields.Boolean()
    Garden = fields.Boolean()
    garden_area = fields.Integer("Garden Area")
    Salesperson= fields.Char()
    Buyer=fields.Char()
    offer_price = fields.Float("Offer Price")
    status_SELECTION = [
        ('Accepted', 'Accepted'),
        ('Refused', 'Refused '),
    ]
    status = fields.Selection(status_SELECTION, string="Status", default='Accepted', Copy=False)
    property_id = fields.Many2one("estate.property", string="partner")
    garden_orientation =[
        ('north', 'north'),
        ('east', 'east'),
        ('south', 'south'),
        ('west', 'west'),
        ]
    garden_orientation=fields.Selection(garden_orientation)
    STATE_SELECTION = [
        ('new', 'New'),
        ('offer_accepted', 'Offer Accepted'),
        ('cancel', 'Cancel'),
        ('sold', 'Sold'),
        ('receive', 'Receive'),
    ]
    state =fields.Selection(STATE_SELECTION, string="State" ,default='new')
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string="Gender")
    property_type_id = fields.Many2one("estateproperty.type", string="Property Type")
    total_area = fields.Float(string="total_area", compute="_compute_total", store=True)
    best_price = fields.Float(string ="Best Offer", compute="_compute_highest_price")
    validity = fields.Integer()
    Deadline = fields.Date()

    @api.depends("garden_area","living_area_SQM")
    def _compute_total(self):
        for value in self:
            value.total_area = value.garden_area + value.living_area_SQM
            return  value.total_area

    def _compute_highest_price(self):
        for record in self:
            record.best_price = max(self.mapped('offer_price'))
