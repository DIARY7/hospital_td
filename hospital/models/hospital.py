# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hospital(models.Model):
    _name = 'hospital.hospital'
    _description = "Information sur un hopital"

    name = fields.Char(string='Nom')
    address = fields.Char(string = "Address")
    patients_id = fields.One2many('hospital.patient', 'hospital_id')


