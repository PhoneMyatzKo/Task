from odoo import models, fields, api
from datetime import timedelta
from dateutil.relativedelta import relativedelta

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    join_date = fields.Date(string="Join Date", required=True)
    probation_end_date = fields.Date(string="Probation End Date", compute='_compute_probation_end_date', store=True)

    @api.depends('join_date')
    def _compute_probation_end_date(self):
        for employee in self:
            if employee.join_date:
                probation_end = employee.join_date + relativedelta(months=3)
                employee.probation_end_date = probation_end
            else:
                employee.probation_end_date = False

    def send_probation_end_emails(self):
        hr_managers = self.env['hr.employee'].search([('job_id.name', '=', 'HR Manager')])
        employees = self.env['hr.employee'].search([])
        today = fields.Date.today()
        for employee in employees:
            if employee.probation_end_date and employee.probation_end_date <= today:
                nametosent = {
                    'Ename': employee.name,
                    'email_from': self.env.company.email
                }
                for manager in hr_managers:
                    email_template = self.env.ref('tid-46.email_template_probation_end')
                    email_template.with_context(data = nametosent).send_mail(manager.id, force_send=True)



    



