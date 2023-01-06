# -*- coding: utf-8 -*-
{
    'name': "test3",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'test1', 'test2'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/cronjob.xml',
        'data/email_template.xml',
        'views/s_indicator_evaluation.xml',
        'views/s_s_hr_department.xml',
        'views/accountant_email.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
