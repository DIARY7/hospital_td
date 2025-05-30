# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DiseaseType(models.Model):
    _name = 'hospital.disease.type'
    _description = 'Type de Disease'

    name = fields.Char()


