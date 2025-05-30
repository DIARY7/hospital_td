from odoo import models,fields

class Symptom(models.Model):
    _name = 'hospital.disease.symptom'
    _description = 'Symptom de maladie'

    name = fields.Text(string='Name')
    severity = fields.Float(string='Severity')