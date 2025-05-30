# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DiseaseType(models.Model):
    _name = 'hospital.disease.type'
    _description = 'Type de Disease'

    name = fields.Char("Name type")
    is_prescription = fields.Boolean("Is prescription") # Misy type de maladie ne necessite pas de prescription


