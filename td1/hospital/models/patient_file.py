# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PatientFile(models.Model):
    _name = 'hospital.patient.file'
    _description = "Fiche d'un patient"

    consultation_id = fields.Many2one("hospital.consultation")





