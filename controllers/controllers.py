# -*- coding: utf-8 -*-
from odoo import http

# class Occasion(http.Controller):
#     @http.route('/occasion/occasion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/occasion/occasion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('occasion.listing', {
#             'root': '/occasion/occasion',
#             'objects': http.request.env['occasion.occasion'].search([]),
#         })

#     @http.route('/occasion/occasion/objects/<model("occasion.occasion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('occasion.object', {
#             'object': obj
#         })