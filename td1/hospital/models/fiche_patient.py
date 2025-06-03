# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FichePatient(models.Model):
    _name = 'hospital.fiche.patient'

    consultation_id = fields.Many2one('hospital.consultation',required=True)
    medication_ids = fields.Many2many('hospital.medication')
    conseil = fields.Char(string='Conseil')




