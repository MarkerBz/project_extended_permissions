# -*- coding: utf-8 -*-

from odoo import api, models


class Users(models.Model):
    _inherit = "res.users"
    
    @api.multi
    def write(self, vals):
        res = super(Users, self).write(vals)
        if vals.get('company_id') or vals.get('company_ids'):
            # Clear cache in 'ir.rule' models:
            access_rule = self.env['ir.rule'].browse(1)
            #access_rule._compute_domain.clear_cache(access_rule)
            access_rule.name = access_rule.name  # it works too!
        return res
