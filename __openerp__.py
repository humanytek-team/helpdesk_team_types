# -*- coding: utf-8 -*-
{
    'name': 'Tipos de ticket por departamento en Helpdesk',
    'version': '1.1',
    'summary': 'Se agrega funcionalidad al modulo de Helpdesk que permite mostrar unicamente los tipos de vale que pertenecen alarea de soporte seleccionada',
    'category': 'Denker',
    'description': """
    Se agrega funcionalidad al modulo de Helpdesk que permite mostrar unicamente los tipos de vale que pertenecen alarea de soporte seleccionada.
    """,
    'author': 'Humanytek',
    'website': 'http://www.humanytek.com',
    'depends': ['helpdesk'],
    'data': [
        'helpdesk_ticket.xml',
        'helpdesk_ticket_type.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
