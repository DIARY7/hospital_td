# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Demand(models.Model):
    _name = 'hospital.demand.patient'
    _description = "Information sur une demande"

    date_of_demand = fields.Date(string='Date of demand')
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    doctor_id = fields.Many2one('hospital.staff.doctor', string='Hospital')




