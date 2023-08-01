{'name': "Real-Estate Management",
 'version': '1.0',
 'depend': ['base'],
 'author': "Osama Imran",
 'category': 'category',
 'description': """ this is a test module of Real-Estate Management!
    written for the odoo Quickstart Tutorial """,
 'data': ['security/ir.model.access.csv',
          'views/estate_properties_views.xml',
          'views/estate_property_type_views.xml',
          'views/estate_property_offer_views.xml'
          ],

 'installable': True,
 'auto_install': False,
 'application': False, }
