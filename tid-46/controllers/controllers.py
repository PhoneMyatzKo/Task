# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-46(http.Controller):
#     @http.route('/tid-46/tid-46', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-46/tid-46/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-46.listing', {
#             'root': '/tid-46/tid-46',
#             'objects': http.request.env['tid-46.tid-46'].search([]),
#         })

#     @http.route('/tid-46/tid-46/objects/<model("tid-46.tid-46"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-46.object', {
#             'object': obj
#         })
