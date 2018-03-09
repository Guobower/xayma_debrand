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
    'company': "Xayma Solutions",
    'website': "http://www.supermalang.com",
    'category': 'Tools',
    'version': '11.0.0.0',
    'depends': ['base'],
    'data': [
        'views/views.xml',
        'views/xayma.debrand.footer.template.xml',
        'views/xayma.debrand.header.xml',
        'views/xayma.debrand.loginpage.xml',
    ],
    'license': "LGPL-3",
    'auto_install': True,
    'application': False
}