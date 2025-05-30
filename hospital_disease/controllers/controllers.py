# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalDisease(http.Controller):
#     @http.route('/hospital_disease/hospital_disease', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_disease/hospital_disease/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_disease.listing', {
#             'root': '/hospital_disease/hospital_disease',
#             'objects': http.request.env['hospital_disease.hospital_disease'].search([]),
#         })

#     @http.route('/hospital_disease/hospital_disease/objects/<model("hospital_disease.hospital_disease"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_disease.object', {
#             'object': obj
#         })

