# -*- coding: utf-8 -*-

#import models   - At the bottom!

from odoo import api, SUPERUSER_ID
import logging

log = logging.getLogger(__name__)


def _cancel_original_global_rules_on_projects_by_company_of_user(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    invert_active_flag_of_original_global_rules(env, current_active=True)

def invert_active_flag_of_original_global_rules(env, current_active):
    external_ids = ['task_comp_rule', 'project_comp_rule', 'analytic_comp_rule']
    external_modules = ['project', 'analytic']
    external_records = env['ir.model.data'].search([
        ('name', 'in', external_ids),
        ('module', 'in', external_modules),
    ])
    if not external_records:
        return
    internal_ids = [r.res_id for r in external_records]
    original_global_rules = env['ir.rule'].search([
        ('id', 'in', internal_ids),
        ('active', '=', current_active),
    ])
    if original_global_rules:
        names = [r.name for r in original_global_rules]
        log.info("Invert 'active' flag of original global rules ('ir.rule') on Projects by Company of User. Ids: {}. Names {}. New 'active' == {}".format \
            (original_global_rules.ids, names, not current_active))
        for rule in original_global_rules:
            rule.active = not rule.active


# Not at the top!
import models
