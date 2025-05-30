# -*- coding: utf-8 -*-
# from odoo import http


# class Hopital-1(http.Controller):
#     @http.route('/hopital-1/hopital-1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hopital-1/hopital-1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hopital-1.listing', {
#             'root': '/hopital-1/hopital-1',
#             'objects': http.request.env['hopital-1.hopital-1'].search([]),
#         })

#     @http.route('/hopital-1/hopital-1/objects/<model("hopital-1.hopital-1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hopital-1.object', {
#             'object': obj
#         })

