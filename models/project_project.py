# -*- coding: utf-8 -*-

from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"
    
    company_ids = fields.Many2many('res.company', 'project_res_company_rel', 'project_id', 'company_id',
                                string='Visible by companies')
