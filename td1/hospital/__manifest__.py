# -*- coding: utf-8 -*-
{
    'name': "hospital-1",
    'description': """
        Un hôpital traite des patients et leur administre des 
        médicaments.
    """,

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hospital_disease',
        'hospital_patient',
        'hospital_staff'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/consultation_views.xml',
        'views/rond_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False
}

