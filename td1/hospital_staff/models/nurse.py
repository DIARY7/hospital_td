# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Nurse(models.Model):
    _name = 'hospital.staff.nurse'
    _description = "Information sur une infirmiere"
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users')



