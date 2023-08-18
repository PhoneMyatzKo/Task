# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-42(http.Controller):
#     @http.route('/tid-42/tid-42', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-42/tid-42/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-42.listing', {
#             'root': '/tid-42/tid-42',
#             'objects': http.request.env['tid-42.tid-42'].search([]),
#         })

#     @http.route('/tid-42/tid-42/objects/<model("tid-42.tid-42"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-42.object', {
#             'object': obj
#         })
