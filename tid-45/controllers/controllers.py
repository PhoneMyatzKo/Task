# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-45(http.Controller):
#     @http.route('/tid-45/tid-45', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-45/tid-45/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-45.listing', {
#             'root': '/tid-45/tid-45',
#             'objects': http.request.env['tid-45.tid-45'].search([]),
#         })

#     @http.route('/tid-45/tid-45/objects/<model("tid-45.tid-45"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-45.object', {
#             'object': obj
#         })
