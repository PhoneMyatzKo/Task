from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # New computed fields
    cost_group = fields.Selection(
        [('greater', 'Cost Greater or Equal Sale price'),
         ('other', 'Others')],
        compute='_compute_cost_group',
        store=True,
        string='Cost Group',
    )

    cost_group_two = fields.Selection(
        [('less', 'Cost Less than Sale price'),
         ('other', 'Others')],
        compute='_compute_cost_group_two',
        store=True,
        string='Cost Group Two',
    )

    @api.depends('standard_price', 'list_price')
    def _compute_cost_group(self):
        for product in self:
            product.standard_price
            product.list_price
            if product.standard_price >= product.list_price:
                product.cost_group = 'greater'
            else:
                product.cost_group = 'other'

    @api.depends('standard_price', 'list_price')
    def _compute_cost_group_two(self):
        for product in self:
            product.standard_price
            product.list_price
            if product.standard_price < product.list_price:
                product.cost_group_two = 'less'
            else:
                product.cost_group_two = 'other'
