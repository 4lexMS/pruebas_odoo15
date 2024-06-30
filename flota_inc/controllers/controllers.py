# -*- coding: utf-8 -*-
# from odoo import http


# class FlotaInc(http.Controller):
#     @http.route('/flota_inc/flota_inc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flota_inc/flota_inc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('flota_inc.listing', {
#             'root': '/flota_inc/flota_inc',
#             'objects': http.request.env['flota_inc.flota_inc'].search([]),
#         })

#     @http.route('/flota_inc/flota_inc/objects/<model("flota_inc.flota_inc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flota_inc.object', {
#             'object': obj
#         })
