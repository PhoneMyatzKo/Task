from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    skip_picking_creation = fields.Boolean(default=False, store=False)

    def _create_picking(self):
        if not self.skip_picking_creation:
            return super()._create_picking()

    def button_approve(self, force=False):
        self.skip_picking_creation = True
        result = super().button_approve(force=force)
        self.skip_picking_creation = False
        return result
    
    
    def action_create_invoice(self):
        self.skip_picking_creation = False
        self._create_picking()
        for order in self:
            for line in order.order_line:
                line.qty_to_invoice = line.product_qty
        res = super(PurchaseOrder, self).action_create_invoice()
        return res