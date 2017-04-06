# -*- coding: utf-8 -*-

from .. import invert_active_flag_of_original_global_rules

from odoo import api, models


class Module(models.Model):
    _inherit = "ir.module.module"
    
    @api.multi
    def module_uninstall(self):
        # Process only current module
        if self.name == __name__.split('.')[2]:
            invert_active_flag_of_original_global_rules(self.env, current_active=False)
        return super(Module, self).module_uninstall()
