# -*- coding: utf-8 -*-
{
    'name': 'Project - Extended permissions in multi-company',
    'version': '10.0.1.0.0',
    'author': 'Contractor Andrey S. 2017',
    'category': 'Project',
    'description': """
Project - Extended permissions
==============================
Extended permissions for Project's stuff in multi-company mode.
    """,
    'depends': [
        'base',
        'project',
        'project_issue',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/project_extended_permissions_security.xml',
        'views/project_project_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'post_init_hook': '_cancel_original_global_rules_on_projects_by_company_of_user',
}
