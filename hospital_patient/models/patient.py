# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = "Information sur une patient"
    _inherit = "res.partner" # Mi heriter nom sy email , etc...

    date_of_birth = fields.Date(string='Date of Birth')
    user_id = fields.Many2one('res.users', string='User')
    hospital_id = fields.Many2one('hospital.hospital', string='Hospital')

    


