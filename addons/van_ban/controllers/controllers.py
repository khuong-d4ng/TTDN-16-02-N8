# -*- coding: utf-8 -*-
# from odoo import http


# class van_ban(http.Controller):
#     @http.route('/van_ban/van_ban', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/van_ban/van_ban/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('van_ban.listing', {
#             'root': '/van_ban/van_ban',
#             'objects': http.request.env['van_ban.van_ban'].search([]),
#         })

#     @http.route('/van_ban/van_ban/objects/<model("van_ban.van_ban"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('van_ban.object', {
#             'object': obj
#         })
