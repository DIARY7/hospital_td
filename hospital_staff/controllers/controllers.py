# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalStaff(http.Controller):
#     @http.route('/hospital_staff/hospital_staff', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_staff/hospital_staff/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_staff.listing', {
#             'root': '/hospital_staff/hospital_staff',
#             'objects': http.request.env['hospital_staff.hospital_staff'].search([]),
#         })

#     @http.route('/hospital_staff/hospital_staff/objects/<model("hospital_staff.hospital_staff"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_staff.object', {
#             'object': obj
#         })

