# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    def open_wame(self):
        print(self.env.context)
        return {
            'name': 'Go to website',
            'res_model': 'ir.actions.act_url',
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://wa.me/{}'.format(self[self.env.context.get('field_name')])
        }
