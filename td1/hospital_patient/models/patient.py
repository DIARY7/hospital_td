# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = "Information sur une patient"
    _inherit = "res.partner" # Mi heriter nom sy email , etc...

    date_of_birth = fields.Date(string='Date of Birth')
    user_id = fields.Many2one('res.users', string='User')
    hospital_id = fields.Many2one('hospital.hospital', string='Hospital')
    state = fields.Selection([
        ('in_remission', "In remission"),
        ('in_treatment', "In treatment"),
        ('free_to_go', "Free to go"),
    ], string="State", default='in_remission', required=True)
    


