# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Nurse(models.Model):
    _name = 'hospital.staff.nurse'
    _description = "Information sur une infirmiere"
    _inherit = 'res.partner'

    user_id = fields.Many2one('res.users')



