# -*- coding: utf-8 -*-
# from odoo import http


# class Incupasaje(http.Controller):
#     @http.route('/incupasaje/incupasaje', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/incupasaje/incupasaje/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('incupasaje.listing', {
#             'root': '/incupasaje/incupasaje',
#             'objects': http.request.env['incupasaje.incupasaje'].search([]),
#         })

#     @http.route('/incupasaje/incupasaje/objects/<model("incupasaje.incupasaje"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('incupasaje.object', {
#             'object': obj
#         })
