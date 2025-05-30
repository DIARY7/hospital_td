# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Rond(models.Model):
    _name = 'hospital.rond'
    _description = "Ronde des infirmières"

    date_of_rond = fields.Date(string='Date of rond')
    nurse_id = fields.Many2one('hospital.staff.nurse', string='Nurse')
    line_rond_ids = fields.One2many('hospital.line.rond', 'rond_id', string='Line rond')



