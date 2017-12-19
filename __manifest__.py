# -*- coding: utf-8 -*-
{
    'name': "Xayma Branding",

    'summary': """
        Enlève sur l'interface utilisateur, les références à Odoo""",

    'description': """
        Enlève les références à Odoo sur l'interface utilisateur, aux emplacements suivants :
        - Footer
        - Login Page
    """,

    'author': "Elhadji Malang DIEDHIOU",
    'website': "http://www.supermalang.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/xayma.debrand.footer.template.xml',
        'views/xayma.debrand.header.xml',
        'views/xayma.debrand.loginpage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}