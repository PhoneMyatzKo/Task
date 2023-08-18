# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-43(http.Controller):
#     @http.route('/tid-43/tid-43', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-43/tid-43/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-43.listing', {
#             'root': '/tid-43/tid-43',
#             'objects': http.request.env['tid-43.tid-43'].search([]),
#         })

#     @http.route('/tid-43/tid-43/objects/<model("tid-43.tid-43"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-43.object', {
#             'object': obj
#         })
