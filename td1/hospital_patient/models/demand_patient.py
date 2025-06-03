# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Demand(models.Model):
    _name = 'hospital.demand.patient'
    _description = "Information sur une demande"

    date_of_demand = fields.Date(string='Date of demand',default=fields.Date.today)
    patient_id = fields.Many2one('hospital.patient', string='Patient',required=True,readonly=True)
    symptom_ids = fields.Many2many("hospital.disease.symptom", string='Symptoms', relation="demand_symptom_rel")

    @api.model
    def default_get(self, fields_list):
        res = super(Demand, self).default_get(fields_list)
        patient = self.env['hospital.patient'].search([('user_id', '=', self.env.uid)], limit=1)

        if not patient:
            raise UserError (_("Aucun patient lié à cet utilisateur."))

        res['patient_id'] = patient.id
        return res


