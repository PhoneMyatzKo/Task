from odoo import fields, models, api, _ 

class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Hr Employee Inherit"

    @api.onchange('department_id')
    def department_id_onchange(self):
        if self.department_id:
            return {
                'domain': 
                {
                    'job_id':[('id','in',self.department_id.jobs_ids.ids)]
                }
            }
