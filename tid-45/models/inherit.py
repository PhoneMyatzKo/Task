from odoo import fields, models, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    apply_cash_down = fields.Boolean(string="Apply Cash Down")


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id.apply_cash_down:
            raise UserError("This customer needs to make payment first!")
        
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id.apply_cash_down:
            raise UserError("This supplier needs to make payment first!")
