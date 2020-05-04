# -*- coding: utf-8 -*-
from odoo import _, api, models


class Partner(models.Model):
    _inherit = 'res.partner'

    def open_wame(self):
        return {
            'name': 'Go to website',
            'res_model': 'ir.actions.act_url',
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://wa.me/{}{}'.format(self.country_id.phone_code, self[self.env.context.get('field_name')])
        }
