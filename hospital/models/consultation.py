# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Consultation(models.Model):
    _name = 'hospital.consultation'
    _description = "Information sur une consultation"

    date_consultation = fields.Date(string='Date of Consultation')
    doctor_id = fields.Many2one('hospital.staff.doctor', string='Doctor')
    demand_patient_id = fields.Many2one('hospital.demand.patient', string='Demand')





