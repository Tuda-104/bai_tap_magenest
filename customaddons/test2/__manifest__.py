# -*- coding: utf-8 -*-
{
    'name': "test2",

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
    'depends': ['base', 'purchase', 'hr'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'demo/hr_department_demo.xml',
        'views/s_hr_department.xml',
        'views/s_purchase_order.xml',
        'views/order_creation.xml',
        'views/order_creation_limit.xml',
        'wizard/report_accountant.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
