from odoo import models, fields, api
import qrcode
import base64
import os

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def generate_qrcode_image(self):
        for info in self:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(info.name)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Save the QR code image in the qrcodes folder inside static
            image_path = os.path.join('Tasks','Task-42', 'static', 'qrcodes', f"{info.name}.png")
            img.save(image_path)

            # Read the image file and convert it to base64
            with open(image_path, 'rb') as image_file:
                info.qrcode_data = base64.b64encode(image_file.read())

    qrcode_data = fields.Binary(string='QR Code Data', compute='generate_qrcode_image')