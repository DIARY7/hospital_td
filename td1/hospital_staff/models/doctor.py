# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Doctor(models.Model):
    _name = 'hospital.staff.doctor'
    _description = "Information sur un Medecin"
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users')






