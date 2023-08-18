# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-47(http.Controller):
#     @http.route('/tid-47/tid-47', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-47/tid-47/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-47.listing', {
#             'root': '/tid-47/tid-47',
#             'objects': http.request.env['tid-47.tid-47'].search([]),
#         })

#     @http.route('/tid-47/tid-47/objects/<model("tid-47.tid-47"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-47.object', {
#             'object': obj
#         })
