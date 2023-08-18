from odoo import models, fields

class MyInheritAccountInvoice(models.Model):
    _inherit = 'account.move'

    vehicle_no = fields.Char(string="Vehicle No")

class MyInheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    vehicle_no = fields.Char(string="Vehicle No")

    def _prepare_invoice(self):
        res = super(MyInheritSaleOrder, self)._prepare_invoice()
        res['vehicle_no'] = self.vehicle_no
        return res
