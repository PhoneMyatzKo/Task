from odoo import fields, models, api

class StockMoveInherit(models.Model):
    _inherit = 'stock.move'

    @api.onchange('location_id')
    def _onchange_location_id(self):
        if self.location_id:
            products = self._get_products_in_location(self.location_id)
            domain = [('id', 'in', products.ids)]
            return {'domain': {'product_id': domain}}

    def _get_products_in_location(self, location):
        products = self.env['product.product']
        quants = self.env['stock.quant'].search([('location_id', '=', location.id)])
        for quant in quants:
            if quant.product_id not in products:
                products += quant.product_id
        return products

