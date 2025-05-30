# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = "Information sur une patient"

    name = fields.Char()
    date_of_birth = fields.Date(string='Date of Birth')
    


