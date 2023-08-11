# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-50(http.Controller):
#     @http.route('/tid-50/tid-50', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-50/tid-50/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-50.listing', {
#             'root': '/tid-50/tid-50',
#             'objects': http.request.env['tid-50.tid-50'].search([]),
#         })

#     @http.route('/tid-50/tid-50/objects/<model("tid-50.tid-50"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-50.object', {
#             'object': obj
#         })
