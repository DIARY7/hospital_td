# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Nurse(models.Model):
    _name = 'hospital.nurse'
    _description = "Information sur une infirmiere"

    name = fields.Char()
    date_of_birth = fields.Date(string='Date of Birth')



