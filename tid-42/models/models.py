# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tid-42(models.Model):
#     _name = 'tid-42.tid-42'
#     _description = 'tid-42.tid-42'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
