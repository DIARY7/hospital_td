# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Disease(models.Model):
    _name = 'hospital.disease'
    _description = "Generalisation d'une maladie"

    name = fields.Char(string="Name Disease")
    disease_type_id = fields.Many2one('hospital.disease.type',string='Type_disease',index=True)
    symptom_ids = fields.Many2many("hospital.disease.symptom",string='Symptoms',relation="disease_symptom_rel")
    severity_disease =fields.Float(string='Severity' , compute='_compute_severity',store=True)

    @api.depends("disease_symptom_ids.severity")
    def _compute_severity(self):
        for disease in self:
            disease.severity_disease = sum(disease.symptom_ids.mapped('severity'))




