from odoo import api, fields, models


class EstateProperties(models.Model):
    _name = "estate.property"
    _description = "Model for Real-Estate Properties"
    _rec_name = 'name'

    tag_ids =fields.Integer()
    my_new_house =fields.Char()
    Title = fields.Char()
    name = fields.Char()
    description = fields.Char()
    postcode = fields.Char()
    bedrooms = fields.Integer()
    data_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    living_area_SQM = fields.Integer()
    availible_form = fields.Date()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    salesperson= fields.Char()
    buyer=fields.Char()
    offer_price = fields.Float()
    status_SELECTION = [
        ('Accepted', 'Accepted'),
        ('Refused', 'Refused '),
    ]
    status = fields.Selection(status_SELECTION, string="status", default='Accepted', Copy=False)
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
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender")
    property_type_id=fields.Char()
    total_area = fields.Float(string="total_area", compute="_compute_total", store=True)
    best_price= fields.Float(string = "best_highest_offer" ,compute="_compute_highest_price")
    validity= fields.Integer()
    Deadline= fields.Date()

    _sql_constraints = [
        ('check_positive_expected_price_value', 'check(selling_price>0)', 'sellingg price must be >0'),
        ('check_positive_expect_price_value', 'check(expected_price>0)', 'expectedd__price must be >0')
    ]

    @api.depends("garden_area","living_area_SQM")
    def _compute_total(self):
        for value in self:
            value.total_area = value.garden_area + value.living_area_SQM
            return  value.total_area

    def _compute_highest_price(self):
        for record in self:
            record.best_price = max(self.mapped('offer_price'))
