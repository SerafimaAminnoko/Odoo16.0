from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Persons(models.Model):
    _name = 'person'
    _description = 'table for storing persons'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    full_name = fields.Char(string='Full Name', compute='_compute_full_name')
    birthday = fields. Date(string='Birthday')
    age = fields.Integer(string='Age', compute='_compute_age')
    sex = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('non-binary', 'Non-binary'),
        ]
    )
    company_id = fields.Many2one(
        "res.company",
        string='Company',
        required = True,
        default=lambda self: self.env.company
    )


    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday and record.birthday <= fields.Date.today():
                record.age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.birthday)
                ).years
            else:
                record.age = 0

    def _compute_full_name(self):
        for record in self:
            record.full_name = record.first_name + ' ' + record.last_name
