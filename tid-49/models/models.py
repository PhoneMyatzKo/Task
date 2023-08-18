from odoo import models, fields, api
from datetime import datetime

class CustomHrEmployee(models.Model):
    _inherit = 'hr.employee'

    age = fields.Integer(string="Age", compute='_compute_age', store=True)

    @api.depends('birthday')
    def _compute_age(self):
        for employee in self:
            if employee.birthday:
                birth_date = fields.Datetime.from_string(employee.birthday)
                today = fields.Date.today()
                delta = today - birth_date.date()
                employee.age = delta.days // 365
            else:
                employee.age = 0
