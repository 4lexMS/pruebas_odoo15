# -*- coding: utf-8 -*-
{
    'name': "flota_inc",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'account', 'contacts', 'hr_expense'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/flota_Incubadora_views.xml',
        'views/flota_SanJose_views.xml',
        'views/flota_Yuluc_views.xml',
        'views/employee_inherit_views.xml',
        'views/expense_inherit_views.xml',
        'views/menus_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
