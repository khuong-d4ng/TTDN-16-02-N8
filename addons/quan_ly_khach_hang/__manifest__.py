# -*- coding: utf-8 -*-
{
    'name': 'Quản lý khách hàng',
    'summary': 'Quản lý khách hàng và đơn hàng',
    'description': '''
        Module quản lý khách hàng và đơn hàng.
        Bao gồm thông tin khách hàng, trạng thái đơn hàng và các số liệu tổng hợp.
    ''',
    'author': 'My Company',
    'website': 'http://www.yourcompany.com',
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/khach_hang_views.xml',
        'views/don_hang_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
