# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-48(http.Controller):
#     @http.route('/tid-48/tid-48', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-48/tid-48/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-48.listing', {
#             'root': '/tid-48/tid-48',
#             'objects': http.request.env['tid-48.tid-48'].search([]),
#         })

#     @http.route('/tid-48/tid-48/objects/<model("tid-48.tid-48"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-48.object', {
#             'object': obj
#         })
