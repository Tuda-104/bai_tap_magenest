{
    'name': "test1",
    'description': "CRM-Sale",
    'author': "By me",
    'website': "https://http://www.example.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'sale',
        'crm',
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/s_sales_team.xml',
        'views/s_custom_crm_lead.xml',
        'views/s_custom_sale_order.xml',
        'views/plan_sale_order.xml',
        'views/indicator_evaluation.xml',
        'wizard/s_report_detailed.xml',
        'wizard/s_report_indicator_evaluation.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}