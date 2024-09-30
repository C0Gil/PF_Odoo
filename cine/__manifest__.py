# -*- coding:utf-8 -*-

{
    'name': 'Modulo de Cine',
    'version': '1.0',
    'depends': [
      'peliculas'
      ],
    'author': 'Gilberto C. O.',
    'category': 'Peliculas',
    'website': 'http://www.google.com',
    'summary': 'Modulo que agrega funcionalidades al modulo de peliculas',
    'description': '''
      Modulo que agrega funcionalidades al modulo de peliculas
    ''',    
    'data': [
      'security/ir.model.access.csv',
      'data/categories.xml',
      'data/sequence.xml',
      'views/ticket_price_view.xml',
      'views/cinema_view.xml',
      'views/cinema_menu.xml',
    ],
}