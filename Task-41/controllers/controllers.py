# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-41(http.Controller):
#     @http.route('/tid-41/tid-41', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-41/tid-41/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-41.listing', {
#             'root': '/tid-41/tid-41',
#             'objects': http.request.env['tid-41.tid-41'].search([]),
#         })

#     @http.route('/tid-41/tid-41/objects/<model("tid-41.tid-41"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-41.object', {
#             'object': obj
#         })
