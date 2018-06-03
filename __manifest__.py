# -*- coding: utf-8 -*-
{
    'name': "Xayma Branding",
    'summary': "Personnalise l'interface de Xayma",
    'description': """
        Met les références à Xayma sur l'interface utilisateur, aux emplacements suivants :
        - Page de connexion
        - Footers
        - Titre de page
        - Favicons
        - Copyrights
        - Warning Dialogues
        - Error Dialogues
        - Wizards
        - Backend pages
    """,
    'author': "Xayma Solutions",
    'website': "http://www.xayma-solutions.com",
    'category': 'Tools',
    'version': '11.0.1.0',
    'depends': ['base'],
    'demo': [],
    'data': [
        'views/xayma.debrand.footer.template.xml',
        'views/xayma.debrand.header.xml',
        'views/xayma.debrand.loginpage.xml',
    ],
    'qweb': ['static/src/xml/base.xml'],
    'installable': True,
}