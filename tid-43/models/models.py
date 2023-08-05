from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # New computed fields
    cost_group = fields.Selection(
        [('greater', 'Cost Greater or Equal Saleprice'),
         ('less', 'Others')],
        compute='_compute_cost_group',
        store=True,
        string='Cost Group',
    )

    cost_group_two = fields.Selection(
        [('greater', 'Others'),
         ('less', 'Cost Less than Saleprice')],
        compute='_compute_cost_group_two',
        store=True,
        string='Cost Group',
    )


    def _compute_cost_group(self):
        for product in self:
            if product.standard_price >= product.list_price:
                product.cost_group = 'greater'
            else:
                product.cost_group = 'less'

    def _compute_cost_group_two(self):
        for product in self:
            if product.standard_price >= product.list_price:
                product.cost_group_two = 'greater'
            else:
                product.cost_group_two = 'less'
