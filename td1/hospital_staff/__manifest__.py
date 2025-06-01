# -*- coding: utf-8 -*-
{
    'name': "hospital_staff",
    'description': """
        Module contenant les staff de l'hopital
    """,

    'author': "Diary",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        'data/security.xml',
        'data/staff_data.xml',
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

