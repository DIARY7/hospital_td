# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LineRond(models.Model):
    _name = 'hospital.line.rond'
    _description = "Information sur un seule ligne de ronde"

    patient_id = fields.Many2one('hospital.patient',string='patient')
    description = fields.Text(string='Description')
    rond_id = fields.Many2one('hospital.rond',string='Rond')




