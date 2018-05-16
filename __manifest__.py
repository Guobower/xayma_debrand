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
    'category': 'Usability',
    'version': '11.0.1.0',
    'depends': ['base'],
    'data': [
        'views/xayma.debrand.footer.template.xml',
        'views/xayma.debrand.header.xml',
        'views/xayma.debrand.loginpage.xml',
    ],
    'demo': [],
}