from odoo import models, api, exceptions

class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    def create_returns(self):
        for wizard in self:
            for line in wizard.product_return_moves:
                if line.quantity > line.move_id.quantity_done:
                    raise exceptions.ValidationError(
                        "Returned quantity cannot be greater than the delivered quantity."
                    )
        return super(StockReturnPicking, self).create_returns()