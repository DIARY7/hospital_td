# -*- coding: utf-8 -*-
{
    'name': "hospital_patient",


    'description': """
        Module qui gère les patients
    """,

    'author': "Diary",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','hospital_staff','hospital_disease'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'data/security.xml',
        'data/patient_data.xml',
        'views/demand_patient_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

