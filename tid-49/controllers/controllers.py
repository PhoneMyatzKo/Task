# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-49(http.Controller):
#     @http.route('/tid-49/tid-49', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-49/tid-49/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-49.listing', {
#             'root': '/tid-49/tid-49',
#             'objects': http.request.env['tid-49.tid-49'].search([]),
#         })

#     @http.route('/tid-49/tid-49/objects/<model("tid-49.tid-49"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-49.object', {
#             'object': obj
#         })
