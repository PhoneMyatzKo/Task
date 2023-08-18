# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-44(http.Controller):
#     @http.route('/tid-44/tid-44', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-44/tid-44/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-44.listing', {
#             'root': '/tid-44/tid-44',
#             'objects': http.request.env['tid-44.tid-44'].search([]),
#         })

#     @http.route('/tid-44/tid-44/objects/<model("tid-44.tid-44"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-44.object', {
#             'object': obj
#         })
