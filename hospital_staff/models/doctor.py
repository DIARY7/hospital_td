# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Doctor(models.Model):
    _name = 'hospital.staff.doctor'
    _description = "Information sur un Medecin"
    _inherit = 'res.partner'






