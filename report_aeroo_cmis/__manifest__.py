# -*- coding: utf-8 -*-
# © 2016 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Aeroo Reports CMIS',
    'version': '10.0.1.0.0',
    'category': 'Generic Modules/Aeroo Reports',
    'author': 'Savoir-faire Linux',
    'website': 'https://www.savoirfairelinux.com',
    'complexity': "easy",
    'depends': ['report_aeroo', 'connector'],
    'data': [
        'views/aeroo_dms_backend.xml',
        'views/ir_actions_report_xml.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    "license": "AGPL-3",
    'installable': False,
    'application': False,
}
