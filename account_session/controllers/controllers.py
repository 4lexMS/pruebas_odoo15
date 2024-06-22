# -*- coding: utf-8 -*-
# from odoo import http


# class AccountSession(http.Controller):
#     @http.route('/account_session/account_session', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_session/account_session/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_session.listing', {
#             'root': '/account_session/account_session',
#             'objects': http.request.env['account_session.account_session'].search([]),
#         })

#     @http.route('/account_session/account_session/objects/<model("account_session.account_session"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_session.object', {
#             'object': obj
#         })
