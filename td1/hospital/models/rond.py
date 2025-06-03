# -*- coding: utf-8 -*-
from odoo import models, fields, api,_
from odoo.exceptions import UserError
class Rond(models.Model):
    _name = 'hospital.rond'
    _description = "Ronde des infirmières"

    date_of_rond = fields.Datetime(string='Date of rond',required=True)
    nurse_id = fields.Many2one('hospital.staff.nurse', string='Nurse')
    line_rond_ids = fields.One2many('hospital.line.rond', 'rond_id', string='Line rond')

    @api.model
    def default_get(self, fields_list):
        res = super(Rond, self).default_get(fields_list)
        nurse = self.env['hospital.staff.nurse'].search([('user_id', '=', self.env.uid)], limit=1)
        if not nurse:
            raise UserError(_("Aucun patient lié à cet utilisateur."))
        res['nurse_id'] = nurse.id
        return res

