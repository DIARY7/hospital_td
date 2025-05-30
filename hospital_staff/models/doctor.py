# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Medecin(models.Model):
    _name = 'hospital.medecin'
    _description = "Information sur un Medecin"

    name = fields.Char()
    date_of_birth = fields.Date(string='Date of Birth')



