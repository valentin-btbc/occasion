# -*- coding: utf-8 -*-
{
    'name': "Véhicule d'occasion",

    'summary': """
        Gestion des véhicule d'occasions.
    """,

    'description': """
        Gestion des véhicule d'occasions.
    """,

    'author': "Noosys",
    'website': "http://www.btbc.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_template_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}