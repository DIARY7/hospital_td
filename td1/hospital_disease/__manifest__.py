# -*- coding: utf-8 -*-
{
    'name': "hospital_disease",

    'description': """
        Module contenant a propos de disease
    """,
    'author': "Diary",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/disease_master_data.xml',
        'data/disease_master_data.xml',
        'security/ir.model.access.csv',
        'views/disease_views.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

